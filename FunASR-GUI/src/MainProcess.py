from PySide6.QtWidgets import QMainWindow, QMenu
from ui.main_ui import Ui_MainWindow
from asr_process import ASRProcess
import os

class MainProcess(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainProcess, self).__init__()
        self.setupUi(self)
        self.m_flag = None
        
        # 初始化各个功能模块
        self.asr_process = ASRProcess(self)
        # self.tts_process = TTSProcess(self)
        # self.audio_process = AudioProcess(self)
        
        # 连接动作信号
        self.act_open_setting_file.triggered.connect(self.open_setting_file)

    def open_setting_file(self):
        """打开配置文件"""
        os.system('gedit FunASR-GUI/FunASR-GUI/config.ini')

    def closeEvent(self, event):
        self.m_flag = False
        if hasattr(self, 'asr_process'):
            self.asr_process.file_controller.cleanup()
        event.accept()
