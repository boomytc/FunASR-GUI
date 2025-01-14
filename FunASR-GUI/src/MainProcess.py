from PySide6.QtWidgets import QMainWindow
from ui.main_ui import Ui_MainWindow
from asr_process import ASRProcess
from tts_process import TTSProcess
from audio_process import AudioProcess

class MainProcess(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainProcess, self).__init__()
        self.setupUi(self)
        self.m_flag = None
        
        # 初始化各个功能模块
        self.asr_process = ASRProcess(self)
        self.tts_process = TTSProcess(self)
        self.audio_process = AudioProcess(self)

    def closeEvent(self, event):
        self.m_flag = False
        # 清理所有模块的资源
        if hasattr(self, 'asr_process'):
            self.asr_process.file_controller.cleanup()
        event.accept()
