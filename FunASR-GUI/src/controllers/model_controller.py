from PySide6.QtWidgets import QMessageBox
from typing import Optional, List
from services.LM_init import ASRModelManager, TTSModelManager
from services.LM_inference import ASRInference, TTSInference
from PySide6.QtCore import QThread, Signal
import os

#ASR模型控制器，负责处理与ASR模型相关的操作和UI交互
class ASRModelController:
    #初始化ASR模型控制器(parent_widget: 父级窗口部件，用于显示消息框)
    def __init__(self, parent_widget=None):
        self.parent_widget = parent_widget
        self.ui_state_manager = parent_widget.ui_state_manager if parent_widget else None
        
        self.model_manager = ASRModelManager()
        self.loading_thread = None
        self.asr_thread = None
        self.batch_asr_thread = None

    #初始化指定的ASR模型(model_name: 要初始化的模型名称 | bool: 初始化是否成功)
    def initialize_model(self, model_name: str) -> None:
        if not model_name or model_name == "请选择语音识别模型":
            return

        # 如果已经有正在运行的线程，先停止它
        if self.loading_thread and self.loading_thread.isRunning():
            self.loading_thread.terminate()
            self.loading_thread.wait()

        if self.ui_state_manager:
            self.ui_state_manager.status_message_changed.emit(f"正在加载模型 {model_name} 中......")
            # 禁用相关控件
            self.ui_state_manager.asr_controls_state_changed.emit(False)
            self.ui_state_manager.batch_controls_state_changed.emit(False)

        self.loading_thread = ModelLoadingThread(self.model_manager, model_name)
        self.loading_thread.finished.connect(self.on_model_loaded)
        self.loading_thread.start()

    def on_model_loaded(self, success: bool, message: str):
        if self.ui_state_manager:
            self.ui_state_manager.status_message_changed.emit(message)
            # 重新启用控件
            self.ui_state_manager.asr_controls_state_changed.emit(True)
            self.ui_state_manager.batch_controls_state_changed.emit(True)

    def disable_controls(self):
        """禁用相关控件"""
        if self.ui_state_manager:
            self.ui_state_manager.asr_controls_state_changed.emit(False)
            self.ui_state_manager.batch_controls_state_changed.emit(False)

    def enable_controls(self):
        """重新启用控件"""
        if self.ui_state_manager:
            self.ui_state_manager.asr_controls_state_changed.emit(True)
            self.ui_state_manager.batch_controls_state_changed.emit(True)

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
        if self.asr_thread and self.asr_thread.isRunning():
            return False, "已有正在进行的识别任务"

        self.asr_thread = ASRProcessThread(
            self.model_manager, 
            audio_path, 
            use_timestamp, 
            distinguish_speaker
        )
        return True, self.asr_thread

    def perform_batch_asr(self, audio_files, use_timestamp=False, distinguish_speaker=False):
        if self.batch_asr_thread and self.batch_asr_thread.isRunning():
            return False, "已有正在进行的批量识别任务"

        self.batch_asr_thread = BatchASRProcessThread(
            self.model_manager,
            audio_files,
            use_timestamp,
            distinguish_speaker
        )
        return True, self.batch_asr_thread

#TTS模型控制器，负责处理与TTS模型相关的操作和UI交互
class TTSModelController:
    def __init__(self, parent_widget=None):
        self.parent_widget = parent_widget

        self.model_manager = TTSModelManager()

    def initialize_model(self, model_name: str) -> bool:
        if not model_name:
            return False

        try:
            if self.parent_widget:
                self.parent_widget.statusbar.showMessage(f"正在加载模型 {model_name} 中......")
            
            self.model_manager.init_model(model_name)

            if self.parent_widget:
                self.parent_widget.statusbar.showMessage(f"模型 {model_name} 初始化成功！")
            return True
        
        except Exception as e:
            if self.parent_widget:
                self.parent_widget.statusbar.showMessage(f"模型初始化失败：{str(e)}")
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

class ModelLoadingThread(QThread):
    finished = Signal(bool, str)  # 成功/失败, 消息

    def __init__(self, model_manager, model_name):
        super().__init__()
        self.model_manager = model_manager
        self.model_name = model_name

    def run(self):
        try:
            self.model_manager.init_model(self.model_name)
            self.finished.emit(True, f"模型 {self.model_name} 初始化成功！")
        except Exception as e:
            self.finished.emit(False, f"模型初始化失败：{str(e)}")

# 添加新的ASR处理线程类
class ASRProcessThread(QThread):
    finished = Signal(bool, str)  # 成功/失败, 结果/错误信息
    progress = Signal(str)  # 用于更新进度信息

    def __init__(self, model_manager, audio_path, use_timestamp, distinguish_speaker):
        super().__init__()
        self.model_manager = model_manager
        self.audio_path = audio_path
        self.use_timestamp = use_timestamp
        self.distinguish_speaker = distinguish_speaker

    def run(self):
        try:
            self.progress.emit("正在处理音频...")
            result = ASRInference.perform_inference(
                self.model_manager,
                self.audio_path,
                use_timestamp=self.use_timestamp,
                distinguish_speaker=self.distinguish_speaker
            )
            self.finished.emit(True, result)
        except Exception as e:
            self.finished.emit(False, str(e))

class BatchASRProcessThread(QThread):
    finished = Signal()  # 批处理完成信号
    progress = Signal(str)  # 进度信息
    file_finished = Signal(bool, str, str)  # 成功/失败, 文件名, 结果/错误信息

    def __init__(self, model_manager, audio_files, use_timestamp, distinguish_speaker):
        super().__init__()
        self.model_manager = model_manager
        self.audio_files = audio_files
        self.use_timestamp = use_timestamp
        self.distinguish_speaker = distinguish_speaker
        self._is_running = True

    def run(self):
        total_files = len(self.audio_files)
        for index, audio_file in enumerate(self.audio_files, 1):
            if not self._is_running:
                break

            file_name = os.path.basename(audio_file)
            self.progress.emit(f"正在处理 ({index}/{total_files}): {file_name}")

            try:
                result = ASRInference.perform_inference(
                    self.model_manager,
                    audio_file,
                    use_timestamp=self.use_timestamp,
                    distinguish_speaker=self.distinguish_speaker
                )
                self.file_finished.emit(True, file_name, result)
            except Exception as e:
                self.file_finished.emit(False, file_name, str(e))

        self.finished.emit()

    def stop(self):
        self._is_running = False