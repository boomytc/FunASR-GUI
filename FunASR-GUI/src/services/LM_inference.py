import torchaudio
import numpy as np
import torch
from utils.content_processer import TextProcessor

class ASRInference:
    @staticmethod
    def format_timestamp(ms):
        """将毫秒转换为 00:00:00,000 格式"""
        seconds = ms / 1000
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = seconds % 60
        milliseconds = int((seconds % 1) * 1000)
        seconds = int(seconds)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

    @staticmethod
    def process_audio(audio_path):
        # 加载音频文件
        waveform, sample_rate = torchaudio.load(audio_path)
        
        # 重采样到16kHz
        if sample_rate != 16000:
            resampler = torchaudio.transforms.Resample(sample_rate, 16000)
            waveform = resampler(waveform)
        
        # 转换为单声道
        if waveform.dim() > 1:
            waveform = waveform.mean(0)
        
        # 转换为float32格式
        waveform = waveform.numpy().astype(np.float32)
        
        return waveform

    @staticmethod
    def format_results(res, use_timestamp=False, distinguish_speaker=False):
        """格式化识别结果"""
        if not use_timestamp:
            return res[0]["text"]
            
        formatted_results = []
        subtitle_index = 1
        
        for result in res:
            if 'sentence_info' in result:
                for sentence in result['sentence_info']:
                    speaker = f"[spk{sentence.get('spk', 'unknown')}]" if distinguish_speaker else ""
                    text = TextProcessor.remove_punctuation(sentence.get('text', ''))
                    start_time = ASRInference.format_timestamp(sentence.get('start', 0))
                    end_time = ASRInference.format_timestamp(sentence.get('end', 0))
                    
                    speaker_text = TextProcessor.format_speaker_text(speaker, text)
                    formatted_results.extend(
                        TextProcessor.format_subtitle_block(subtitle_index, start_time, end_time, speaker_text)
                    )
                    subtitle_index += 1
                    
            elif 'timestamp' in result:
                speaker = f"[spk{result.get('spk', 'unknown')}]" if distinguish_speaker else ""
                text = TextProcessor.remove_punctuation(result.get('text', ''))
                
                for ts in result['timestamp']:
                    start_time = ASRInference.format_timestamp(ts[0])
                    end_time = ASRInference.format_timestamp(ts[1])
                    
                    speaker_text = TextProcessor.format_speaker_text(speaker, text)
                    formatted_results.extend(
                        TextProcessor.format_subtitle_block(subtitle_index, start_time, end_time, speaker_text)
                    )
                    subtitle_index += 1
            else:
                formatted_results.extend(
                    TextProcessor.format_subtitle_block(
                        subtitle_index,
                        "00:00:00,000",
                        "00:00:00,000",
                        result.get('text', '')
                    )
                )
                subtitle_index += 1
                
        return "\n".join(formatted_results)

    @staticmethod
    def perform_inference(model_manager, audio_path, use_timestamp=False, distinguish_speaker=False):
        """执行语音识别推理"""
        # 处理音频
        waveform = ASRInference.process_audio(audio_path)
        
        # 配置推理参数
        inference_config = {
            "batch_size_s": 360,
            "num_workers": 13,
            "use_gpu": False,
            "device_id": -1,
            "cache_size": 204800,
            "chunk_size": 1600,
            "language": "zh",
            "use_itn": True,
            "merge_vad": True
        }
        
        # 执行推理
        result = model_manager.inference(
            waveform,
            **inference_config
        )
        
        # 格式化结果
        formatted_result = ASRInference.format_results(
            result, 
            use_timestamp=use_timestamp,
            distinguish_speaker=distinguish_speaker
        )
        
        # 清理缓存
        ASRInference.cleanup()
        
        return formatted_result

    @staticmethod
    def cleanup():
        if hasattr(torch.cuda, 'empty_cache'):
            torch.cuda.empty_cache()

class TTSInference:
    pass