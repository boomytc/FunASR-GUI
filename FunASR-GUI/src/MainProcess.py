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
        self.btn_asrResultDirSelect.clicked.connect(self.select_asr_result_dir)
        self.chkbox_asrResultSave.stateChanged.connect(self.asr_result_save_state)
        self.btn_asrResultDirOpen.clicked.connect(self.open_asr_result_dir)

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
        self.m_flag = False
        self.file_controller.cleanup() 
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

    #ASR结果保存开启状态
    def asr_result_save_state(self):
        if self.chkbox_asrResultSave.isChecked():
            self.groupBox_asrSave.setEnabled(True)
            # 将默认目录逻辑移到FileController
            if not self.lineEdit_asrSavaDir.text():
                default_dir = self.file_controller.get_default_save_directory()
                self.lineEdit_asrSavaDir.setText(default_dir)
        else:
            self.groupBox_asrSave.setEnabled(False)

    #选择ASR结果保存目录
    def select_asr_result_dir(self):
        """选择ASR结果保存目录"""
        current_dir = self.lineEdit_asrSavaDir.text()
        success, result = self.file_controller.select_asr_save_directory(current_dir)
        
        if success:
            self.lineEdit_asrSavaDir.setText(result)
        elif not isinstance(result, str):
            # 如果返回的是错误信息而不是当前目录
            QMessageBox.critical(self, "错误", result)

    #打开ASR结果保存目录
    def open_asr_result_dir(self):
        """打开ASR结果保存目录"""
        target_dir = self.lineEdit_asrSavaDir.text()
        success, error_msg = self.file_controller.open_asr_save_directory(target_dir)
        
        if not success:
            QMessageBox.critical(self, "错误", error_msg)

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
            
            if self.chkbox_asrResultSave.isChecked():
                save_dir = self.lineEdit_asrSavaDir.text()
                save_mode = 'txt' if self.radioBtn_asrSaveTxtMode.isChecked() else 'srt'
                save_success, save_path = self.file_controller.save_asr_result(result, save_dir, save_mode)
                
                self.lab_asrSaveMessage.setText(
                    f"成功保存 {os.path.basename(save_path)}" if save_success 
                    else f"保存失败：{save_path}"
                )
        else:
            QMessageBox.critical(self, "错误", result)

    #清除语音识别结果
    def clear_asr(self):
        self.txtEdit_result.clear()
