import os
import torch
from funasr import AutoModel
from PySide6.QtCore import QSettings

class ASRModelManager:
    def __init__(self):
        # 使用 QSettings 读取配置
        self.settings = QSettings('FunASR', 'FunASR-GUI')
        
        # 初始化模型配置
        self.model = None
        self.init_model_configs()
        
        # 从配置读取线程设置
        omp_threads = self.settings.value('ThreadSettings/omp_threads', '12')
        mkl_threads = self.settings.value('ThreadSettings/mkl_threads', '12')
        torch_threads = self.settings.value('ThreadSettings/torch_threads', '12')
        
        os.environ['OMP_NUM_THREADS'] = omp_threads
        os.environ['MKL_NUM_THREADS'] = mkl_threads
        torch.set_num_threads(int(torch_threads))

    def init_model_configs(self):
        # 从配置读取基础路径
        base_dir = self.settings.value('ModelPaths/base_dir', '/media/fl01/data01/WorkSpace/FunASR/model')
        
        # 从配置读取模型路径
        model_paraformer = self.settings.value('ModelConfigs/model_paraformer', 
            'speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch')
        model_paraformer_hotwords = self.settings.value('ModelConfigs/model_paraformer_hotwords',
            'speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch')
        vad_model = self.settings.value('ModelConfigs/vad_model',
            'speech_fsmn_vad_zh-cn-16k-common-pytorch')
        punc_model = self.settings.value('ModelConfigs/punc_model',
            'punc_ct-transformer_zh-cn-common-vocab272727-pytorch')
        spk_model = self.settings.value('ModelConfigs/spk_model',
            'speech_campplus_sv_zh-cn_16k-common')
        
        # 定义模型配置
        self.MODEL_CONFIGS = {
            "Paraformer语音识别-中文-通用-16k-离线-large-长音频版模型": {
                "model": f"{base_dir}/{model_paraformer}",
                "vad_model": f"{base_dir}/{vad_model}",
                "punc_model": f"{base_dir}/{punc_model}",
                "spk_model": f"{base_dir}/{spk_model}",
            },
            "Paraformer语音识别-中文-通用-16k-离线-large-长音频版模型(热词版)": {
                "model": f"{base_dir}/{model_paraformer_hotwords}",
                "vad_model": f"{base_dir}/{vad_model}",
                "punc_model": f"{base_dir}/{punc_model}",
                "spk_model": f"{base_dir}/{spk_model}",
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

    def inference(self, waveform, **kwargs):
        """执行推理
        Args:
            waveform: 音频波形数据
            **kwargs: 其他推理参数
        Returns:
            推理结果
        """
        return self.model.generate(
            input=waveform,
            cache={},
            **kwargs
        )

class TTSModelManager:
    pass