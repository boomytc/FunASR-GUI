import os
import torch
from funasr import AutoModel

class ModelManager:
    def __init__(self):
        # 初始化模型配置
        self.model = None
        self.init_model_configs()
        
        # 设置环境变量和torch配置
        os.environ['OMP_NUM_THREADS'] = '12'
        os.environ['MKL_NUM_THREADS'] = '12'
        torch.set_num_threads(12)

    def init_model_configs(self):
        # 初始化模型配置
        model_pwd_dir = "/Users/boom/workspace/FunASR/models"
        
        # 定义模型配置
        self.MODEL_CONFIGS = {
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

    def get_model_names(self):
        return list(self.MODEL_CONFIGS.keys())

    def is_model_initialized(self):
        return self.model is not None

    def init_model(self, model_name):
        # 如果已经有模型实例，先清理
        if self.model is not None:
            del self.model
            self.model = None
            
        # 获取选中模型的配置
        config = self.MODEL_CONFIGS[model_name]
        
        # 初始化新模型
        self.model = AutoModel(
            disable_update=True,
            model=config["model"],
            vad_model=config["vad_model"],
            vad_kwargs={
                "max_single_segment_time": 60000,
                "batch_size": 12,
                "num_workers": 13
            },
            punc_model=config["punc_model"],
            spk_model=config["spk_model"],
        )

    def inference(self, waveform):
        inference_config = {
            "batch_size_s": 360,
            "num_workers": 13,
            "use_gpu": False,
            "device_id": -1,
            "cache_size": 204800,
            "chunk_size": 1600,
        }
        
        return self.model.generate(
            input=waveform,
            cache={},
            language="zh",
            use_itn=True,
            merge_vad=True,
            **inference_config
        )

