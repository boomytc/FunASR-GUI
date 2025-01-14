from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QPushButton, QWidget
import sys
import os
import torchaudio
import numpy as np
import torch

sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'services'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'controllers'))
from ui.main_ui import Ui_MainWindow
from services.LM_init import ModelManager
from services.LM_inference import ASRInference
from utils.ffmpeg_utils import FFmpegUtils
from controllers.model_controller import ModelController
from controllers.file_controller import FileController

class MainProcess(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainProcess, self).__init__()
        self.setupUi(self)
        self.m_flag = None
        self.audio_file_path = None
        
        # 创建控制器实例
        self.model_controller = ModelController(self)
        self.file_controller = FileController(self)
        
        # 设置ComboBox
        self.setup_model_combobox()
        
        # 连接信号
        self.combox_modelSelect.currentIndexChanged.connect(self.model_init)
        self.btn_upload_audio.clicked.connect(self.upload_audio)
        self.btn_asr.clicked.connect(self.asr)
        self.btn_asr_clear.clicked.connect(self.clear_asr)
        self.radiobtn_timestampY.clicked.connect(self.timestamp_mode)
        self.radiobtn_timestampN.clicked.connect(self.timestamp_mode)
        self.radiobtn_spkY.clicked.connect(self.spk_mode)
        self.radiobtn_spkN.clicked.connect(self.spk_mode)

    #设置模型ComboBox
    def setup_model_combobox(self):
        # 清空ComboBox
        self.combox_modelSelect.clear()
        # 添加一个空选项
        self.combox_modelSelect.addItem("")
        # 从控制器获取模型列表
        self.combox_modelSelect.addItems(self.model_controller.get_model_names())

    def model_init(self):
        # 获取当前选择的模型名称
        current_model = self.combox_modelSelect.currentText()
        # 使用控制器初始化模型
        self.model_controller.initialize_model(current_model)

    def closeEvent(self, event):
        # 在关闭窗口时，释放资源
        self.m_flag = False
        FFmpegUtils._cleanup_temp_files()  # 清理临时文件
        event.accept()

    #处理音频文件上传
    def upload_audio(self):
        success, result = self.file_controller.upload_audio()
        if success:
            self.audio_file_path = result  # 保存处理后的临时文件路径
            # 显示原始文件名
            original_filename = self.file_controller.get_original_filename()
            self.label_audioname.setText(original_filename)
        else:
            QMessageBox.critical(self, "错误", result)

    #语音识别处理
    def asr(self):
        # 使用文件控制器检查音频文件
        if not self.file_controller.get_current_audio_path():
            QMessageBox.warning(self, "警告", "请先选择音频文件！")
            return
        
        # 获取时间戳和说话人模式设置
        use_timestamp = self.radiobtn_timestampY.isChecked()
        distinguish_speaker = self.radiobtn_spkY.isChecked()
        
        # 执行语音识别
        success, result = self.model_controller.perform_asr(
            self.audio_file_path,
            use_timestamp=use_timestamp,
            distinguish_speaker=distinguish_speaker
        )
        
        if success:
            self.txtEdit_result.setText(result)
        else:
            QMessageBox.critical(self, "错误", result)

    #清除语音识别结果
    def clear_asr(self):
        self.txtEdit_result.clear()

    #设置时间戳模式
    def timestamp_mode(self):
        if self.radiobtn_timestampY.isChecked():
            pass
        elif self.radiobtn_timestampN.isChecked():
            pass

    #设置说话人模式
    def spk_mode(self):
        if self.radiobtn_spkY.isChecked():
            pass
        elif self.radiobtn_spkN.isChecked():
            pass