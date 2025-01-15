import os
import torch
from funasr import AutoModel
from PySide6.QtCore import QSettings

#语音识别模型管理器
class ASRModelManager:
    def __init__(self):
        # 使用 QSettings 读取配置
        self.settings = QSettings('FunASR', 'FunASR-GUI')
        
        # 获取应用程序的路径
        app_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        config_path = os.path.join(app_path, 'config.ini')
        
        # 确保使用自定义的配置文件
        if os.path.exists(config_path):
            self.settings = QSettings(config_path, QSettings.Format.IniFormat)
        else:
            raise ValueError(f"配置文件不存在：{config_path}")
        
        # 初始化模型配置
        self.model = None
        self.init_model_configs()
        
        # 从配置读取线程设置
        omp_threads = self.settings.value('ASRThreadSettings/omp_threads')
        mkl_threads = self.settings.value('ASRThreadSettings/mkl_threads')
        torch_threads = self.settings.value('ASRThreadSettings/torch_threads')
        
        os.environ['OMP_NUM_THREADS'] = omp_threads
        os.environ['MKL_NUM_THREADS'] = mkl_threads
        torch.set_num_threads(int(torch_threads))

        self.current_model_name = None  # 添加当前模型名称属性

    def init_model_configs(self):
        # 从配置读取基础路径
        base_dir = self.settings.value('ASRModelPaths/base_dir')
        
        # 从配置读取模型路径
        model_paraformer = self.settings.value('ASRModelConfigs/model_paraformer')
        model_paraformer_hotwords = self.settings.value('ASRModelConfigs/model_paraformer_hotwords')
        vad_model = self.settings.value('ASRModelConfigs/vad_model')
        punc_model = self.settings.value('ASRModelConfigs/punc_model')
        spk_model = self.settings.value('ASRModelConfigs/spk_model')
        
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
            
        # 保存当前模型名称
        self.current_model_name = model_name
            
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

    def get_current_model_name(self):
        """获取当前已初始化的模型名称"""
        return self.current_model_name

#语音合成模型管理器
class TTSModelManager:
    def __init__(self):
        self.settings = QSettings('FunASR', 'FunASR-GUI')

        self.model = None
        self.init_model_configs()

        omp_threads = self.settings.value('TTSThreadSettings/omp_threads')
        mkl_threads = self.settings.value('TTSThreadSettings/mkl_threads')
        torch_threads = self.settings.value('TTSThreadSettings/torch_threads')
        
        os.environ['OMP_NUM_THREADS'] = omp_threads
        os.environ['MKL_NUM_THREADS'] = mkl_threads
        torch.set_num_threads(int(torch_threads))

    def init_model_configs(self):
        base_dir = self.settings.value('TTSModelPaths/base_dir')

        model_cosyvoice_300M = self.settings.value('TTSModelConfigs/model_cosyvoice_300M')
        model_cosyvoice_300M_25Hz = self.settings.value('TTSModelConfigs/model_cosyvoice_300M_25Hz')
        model_cosyvoice_300M_instruct = self.settings.value('TTSModelConfigs/model_cosyvoice_300M_instruct')
        model_cosyvoice_300M_SFT = self.settings.value('TTSModelConfigs/model_cosyvoice_300M_SFT')
        model_cosyvoice2_0_5B = self.settings.value('TTSModelConfigs/model_cosyvoice2_0_5B')

        self.MODEL_CONFIGS = {
            "CosyVoice-300M": f"{base_dir}/{model_cosyvoice_300M}",
            "CosyVoice-300M-25Hz": f"{base_dir}/{model_cosyvoice_300M_25Hz}",
            "CosyVoice-300M-Instruct": f"{base_dir}/{model_cosyvoice_300M_instruct}",
            "CosyVoice-300M-SFT": f"{base_dir}/{model_cosyvoice_300M_SFT}",
            "CosyVoice2-0.5B": f"{base_dir}/{model_cosyvoice2_0_5B}",
        }

    def get_model_names(self):
        return list(self.MODEL_CONFIGS.keys())

    def is_model_initialized(self):
        return self.model is not None

    def init_model(self, model_name):
        pass