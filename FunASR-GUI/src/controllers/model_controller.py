from PySide6.QtWidgets import QMessageBox
from typing import Optional, List
from services.LM_init import ASRModelManager, TTSModelManager
from services.LM_inference import ASRInference, TTSInference

#ASR模型控制器，负责处理与ASR模型相关的操作和UI交互
class ASRModelController:
    #初始化ASR模型控制器(parent_widget: 父级窗口部件，用于显示消息框)
    def __init__(self, parent_widget=None):
        self.parent_widget = parent_widget
        # 在控制器中创建模型管理器实例
        self.model_manager = ASRModelManager()

    #初始化指定的ASR模型(model_name: 要初始化的模型名称 | bool: 初始化是否成功)
    def initialize_model(self, model_name: str) -> bool:
        if not model_name:
            return False
            
        try:
            # 初始化模型
            self.model_manager.init_model(model_name)
            
            # 显示成功提示
            if self.parent_widget:
                QMessageBox.information(
                    self.parent_widget,
                    "提示",
                    f"模型 {model_name} 初始化成功！"
                )
            return True
            
        except Exception as e:
            # 显示错误信息
            if self.parent_widget:
                QMessageBox.critical(
                    self.parent_widget,
                    "错误",
                    f"模型初始化失败：{str(e)}"
                )
            return False

    #获取当前已初始化的模型名称(str: 已初始化的模型名称 | None: 未初始化)
    def get_initialized_model(self) -> Optional[str]:
        return self.model_manager.get_current_model_name()

    #检查模型是否已经初始化并可用(bool: 模型是否可用)
    def is_model_ready(self) -> bool:
        return self.model_manager.is_model_initialized()
        
    #获取所有可用模型名称列表(List[str]: 模型名称列表)
    def get_model_names(self) -> List[str]:
        return self.model_manager.get_model_names()
        
    #执行模型推理(audio_data: 音频数据 | 返回值：推理结果)
    def inference(self, audio_data):
        return self.model_manager.inference(audio_data)

    #执行语音识别(audio_path: 音频文件路径 | 返回值：Tuple[bool, str]: 是否成功, 识别结果或错误信息)
    def perform_asr(self, audio_path, use_timestamp=False, distinguish_speaker=False):
        try:
            if not self.is_model_ready():
                return False, "模型未初始化"
                
            result = ASRInference.perform_inference(
                self.model_manager, 
                audio_path,
                use_timestamp=use_timestamp,
                distinguish_speaker=distinguish_speaker
            )
            
            if result:
                return True, result
            return False, "未能识别出文本"
            
        except Exception as e:
            return False, f"识别失败：{str(e)}"

#TTS模型控制器，负责处理与TTS模型相关的操作和UI交互
class TTSModelController:
    def __init__(self, parent_widget=None):
        self.parent_widget = parent_widget

        self.model_manager = TTSModelManager()

    def initialize_model(self, model_name: str) -> bool:
        if not model_name:
            return False

        try:
            self.model_manager.init_model(model_name)

            if self.parent_widget:
                QMessageBox.information(
                    self.parent_widget,
                    "提示",
                    f"模型 {model_name} 初始化成功！"
                )
            return True
        
        except Exception as e:
            if self.parent_widget:
                QMessageBox.critical(
                    self.parent_widget,
                    "错误",
                    f"模型初始化失败：{str(e)}"
                )
            return False

    def get_initialized_model(self) -> Optional[str]:
        return self.model_manager.get_current_model_name()

    def is_model_ready(self) -> bool:
        return self.model_manager.is_model_initialized()
    
    def get_model_names(self) -> List[str]:
        return self.model_manager.get_model_names()
    
    def inference(self, text: str, **kwargs):
        # return self.model_manager.inference(text, **kwargs)
        pass