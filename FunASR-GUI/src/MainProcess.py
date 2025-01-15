from PySide6.QtWidgets import QMainWindow, QMenu
from ui.main_ui import Ui_MainWindow
from ui.ui_state_manager import UIStateManager_ASR
from asr_process import ASRProcess
import os

class MainProcess(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainProcess, self).__init__()
        self.setupUi(self)
        self.m_flag = None
        
        # 初始化UI状态管理器
        self.ui_state_manager = UIStateManager_ASR(self)
        
        # 初始化各个功能模块
        self.asr_process = ASRProcess(self.ui_state_manager)
        
        # 连接动作信号
        self.act_open_setting_file.triggered.connect(self.open_setting_file)
        
        # 连接ASR相关的信号槽
        self.connect_asr_signals()

    def connect_asr_signals(self):
        """连接所有ASR相关的信号槽"""
        # asr模型选择
        self.combox_modelSelect.currentIndexChanged.connect(self.asr_process.model_init_single)
        self.combox_modelSelect_batch.currentIndexChanged.connect(self.asr_process.model_init_batch)
        
        # asr单文件处理
        self.btn_upload_audio.clicked.connect(self.asr_process.upload_audio)
        self.btn_asr.clicked.connect(self.asr_process.asr)
        self.btn_asr_clear.clicked.connect(self.asr_process.clear_asr)
        self.btn_asrResultDirSelect.clicked.connect(self.asr_process.select_asr_result_dir)
        self.chkbox_asrResultSave.stateChanged.connect(self.asr_process.asr_result_save_state)
        self.btn_asrResultDirOpen.clicked.connect(self.asr_process.open_asr_result_dir)

        # asr批量处理
        self.btn_batch_asr_inputDir_select.clicked.connect(self.asr_process.select_batch_input_dir)
        self.btn_batch_asr_outputDir_select.clicked.connect(self.asr_process.select_batch_output_dir)
        self.btn_batch_asr_inputDir_open.clicked.connect(self.asr_process.open_batch_input_dir)
        self.btn_batch_asr_outputDir_open.clicked.connect(self.asr_process.open_batch_output_dir)
        self.btn_batch_asr.clicked.connect(self.asr_process.batch_asr)

    def open_setting_file(self):
        """打开配置文件"""
        os.system('gedit FunASR-GUI/FunASR-GUI/config.ini')

    def closeEvent(self, event):
        self.m_flag = False
        if hasattr(self, 'asr_process'):
            self.asr_process.file_controller.cleanup()
        event.accept()
