# coding=utf-8

import os
import librosa
import gradio as gr
import numpy as np
import torch
import torchaudio
from funasr import AutoModel
import datetime
import torch.multiprocessing as mp
from functools import lru_cache
import time
import psutil  # 如果需要监控系统资源

model_pwd_dir = "/Users/boom/workspace/FunASR/models"

MODEL_CONFIGS = {
	"Paraformer语音识别-中文-通用-16k-离线-large-长音频版模型": {
		"model": f"{model_pwd_dir}/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
		"vad_model": f"{model_pwd_dir}/speech_fsmn_vad_zh-cn-16k-common-pytorch",
		"punc_model": f"{model_pwd_dir}/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
		"spk_model": f"{model_pwd_dir}/speech_campplus_sv_zh-cn_16k-common",
	},
	"Paraformer语音识别-中文-通用-16k-离线-large-长音频版模型(热词版)": {
		"model": f"{model_pwd_dir}/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
		"vad_model": f"{model_pwd_dir}/speech_fsmn_vad_zh-cn-16k-common-pytorch",
		"punc_model": f"{model_pwd_dir}/punc_ct-transformer_zh-cn-common-vocab272727-pytorch",
		"spk_model": f"{model_pwd_dir}/speech_campplus_sv_zh-cn_16k-common",
	}
}

def format_timestamp(ms):
	"""将毫秒转换为 00:00:00,000 格式"""
	seconds = ms / 1000
	hours = int(seconds // 3600)
	minutes = int((seconds % 3600) // 60)
	seconds = seconds % 60
	milliseconds = int((seconds % 1) * 1000)
	seconds = int(seconds)
	return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

# 设置更激进的环境变量和torch配置
os.environ['OMP_NUM_THREADS'] = '12'  # 预留2个核心给系统
os.environ['MKL_NUM_THREADS'] = '12'
torch.set_num_threads(12)

@lru_cache(maxsize=1)  # 减少模型缓存数量，释放更多内存
def load_model(model_name="Paraformer语音识别-中文-通用-16k-离线-large-长音频版模型"):
	"""根据选择加载指定的模型配置"""
	config = MODEL_CONFIGS[model_name]
	model = AutoModel(
		disable_update=True,
		model=config["model"],
		vad_model=config["vad_model"],
		vad_kwargs={
			"max_single_segment_time": 60000,  # 增加单段处理时间
			"batch_size": 12,  # 增加批处理大小
			"num_workers": 13   # 增加工作进程数
		},
		punc_model=config["punc_model"],
		spk_model=config["spk_model"],
	)
	return model

def monitor_resources():
	"""监控系统资源使用情况"""
	cpu_percent = psutil.cpu_percent(interval=1)
	memory = psutil.virtual_memory()
	print(f"CPU使用率: {cpu_percent}%")
	print(f"内存使用率: {memory.percent}%")
	print(f"可用内存: {memory.available / 1024 / 1024:.2f} MB")

def get_optimal_batch_size(audio_length):
	"""根据音频长度动态调整batch_size"""
	if audio_length < 60:  # 短音频
		return 120
	elif audio_length < 300:  # 中等长度
		return 240
	else:  # 长音频
		return 360

def model_inference(input_wav, language, mode="normal", distinguish_speaker=True, 
				   model_name="Paraformer语音识别-中文-通用-16k-离线-large-长音频版模型", fs=16000):
	global model
	# 如果选择的模型与当前加载的不同，重新加载模型
	if not hasattr(model_inference, 'current_model') or model_inference.current_model != model_name:
		model = load_model(model_name)
		model_inference.current_model = model_name
	
	language_abbr = {"zh": "zh"}
	language = "zh"
	selected_language = language_abbr[language]
	
	if isinstance(input_wav, tuple):
		fs, input_wav = input_wav
		# 先进行重采样，再转换为float16
		input_wav = torch.tensor(input_wav, dtype=torch.float32) / 32768.0
		if input_wav.dim() > 1:
			input_wav = input_wav.mean(-1)
		if fs != 16000:
			resampler = torchaudio.transforms.Resample(fs, 16000)
			input_wav = resampler(input_wav.unsqueeze(0)).squeeze(0)
		
		# 重采样后再转换为float16
		input_wav = input_wav.to(torch.float16)
		input_wav = input_wav.numpy().astype(np.float32)  # 转回float32进行推理

	merge_vad = True
	print(f"language: {language}, merge_vad: {merge_vad}, mode: {mode}")
	
	# 更激进的批处理参数
	inference_config = {
		"batch_size_s": 360,    # 显著增加批处理大小
		"num_workers": 13,      # 增加工作进程数
		"use_gpu": False,
		"device_id": -1,
		"cache_size": 204800,   # 增加缓存大小
		"chunk_size": 1600,     # 调整分块大小
	}
	
	monitor_resources()  # 开始时监控
	
	if mode == "normal":
		text = model.generate(
			input=input_wav,
			cache={},
			language=language,
			use_itn=True,
			merge_vad=merge_vad,
			**inference_config
		)
		return text[0]["text"]
	else:  # timestamp mode
		res = model.generate(
			input=input_wav,
			cache={},
			language=language,
			use_itn=True,
			merge_vad=merge_vad,
			timestamp=True,
			**inference_config
		)
		
		formatted_results = []
		subtitle_index = 1
		
		for result in res:
			if 'sentence_info' in result:
				for sentence in result['sentence_info']:
					speaker = f"[spk{sentence.get('spk', 'unknown')}]" if distinguish_speaker else ""
					text = sentence.get('text', '').rstrip(',.。，!！?？') # 去除句尾标点
					start_time = format_timestamp(sentence.get('start', 0))
					end_time = format_timestamp(sentence.get('end', 0))
					
					formatted_results.append(str(subtitle_index))
					formatted_results.append(f"{start_time} --> {end_time}")
					formatted_results.append(f"{speaker} {text}")
					formatted_results.append("")
					subtitle_index += 1
					
			elif 'timestamp' in result:
				speaker = f"[spk{result.get('spk', 'unknown')}]" if distinguish_speaker else ""
				text = result.get('text', '').rstrip(',.。，!！?？') # 去除句尾标点
				
				for ts in result['timestamp']:
					start_time = format_timestamp(ts[0])
					end_time = format_timestamp(ts[1])
					
					formatted_results.append(str(subtitle_index))
					formatted_results.append(f"{start_time} --> {end_time}")
					formatted_results.append(f"{speaker} {text}")
					formatted_results.append("")
					subtitle_index += 1
			else:
				formatted_results.append(str(subtitle_index))
				formatted_results.append("00:00:00,000 --> 00:00:00,000")
				formatted_results.append(result.get('text', ''))
				formatted_results.append("")
				subtitle_index += 1
		
		monitor_resources()  # 结束时监控
		
		return "\n".join(formatted_results)

	# 添加内存回收
	if hasattr(torch.cuda, 'empty_cache'):
		torch.cuda.empty_cache()

html_content = """
<div>
    <h2 style="font-size: 22px;margin-left: 0px;">使用说明</h2>
    <p style="font-size: 18px;margin-left: 20px;">上传音频文件或通过麦克风输入，然后配置语言和识别模式。音频将被转录为相应的文本。</p>
</div>
"""


def launch():
	with gr.Blocks(theme=gr.themes.Soft()) as demo:
		gr.HTML(html_content)
		with gr.Row():
			with gr.Column():
				audio_inputs = gr.Audio(label="上传音频或使用麦克风")
				
				with gr.Accordion("配置"):
					with gr.Row():
						language_inputs = gr.Dropdown(
							choices=["zh"],
							value="zh",
							label="语言",
							scale=1
						)
						mode_inputs = gr.Dropdown(
							choices=["normal", "timestamp"],
							value="normal",
							label="识别模式",
							scale=1
						)
						with gr.Column():
							distinguish_speaker_inputs = gr.Radio(
								choices=["是", "否"],
								value="是",
								label="说话人模式",
								scale=1
							)
                        
					with gr.Row():
						model_inputs = gr.Dropdown(
							choices=list(MODEL_CONFIGS.keys()),
							value=list(MODEL_CONFIGS.keys())[0],
							label="模型选择",
							scale=1
						)
				
				fn_button = gr.Button("开始识别", variant="primary")
				text_outputs = gr.Textbox(label="识别结果")
		
		fn_button.click(
			lambda *args: model_inference(
				args[0], 
				args[1], 
				args[2], 
				args[3] == "是",
				args[4]
			),
			inputs=[audio_inputs, language_inputs, mode_inputs, distinguish_speaker_inputs, model_inputs], 
			outputs=text_outputs
		)

	demo.launch()


if __name__ == "__main__":
	# iface.launch()
	launch()

