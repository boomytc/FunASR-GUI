from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QPushButton, QWidget
import sys
import os

# 先添加路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'services'))

# 然后再导入
from ui.main_ui import Ui_MainWindow
from services.LM_init import ModelManager
import torchaudio
import numpy as np
import torch

class MainProcess(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainProcess, self).__init__()
        self.setupUi(self)
        self.m_flag = None
        self.audio_file_path = None  # 保存音频文件完整路径
        
        # 创建模型管理器实例
        self.model_manager = ModelManager()
        
        # 设置ComboBox
        self.setup_model_combobox()
        
        # 连接信号
        self.combox_modelSelect.currentIndexChanged.connect(self.model_init)
        self.btn_upload_audio.clicked.connect(self.upload_audio)
        self.btn_asr.clicked.connect(self.asr)

    def setup_model_combobox(self):
        # 清空ComboBox
        self.combox_modelSelect.clear()
        # 添加一个空选项
        self.combox_modelSelect.addItem("")
        # 添加所有模型选项
        self.combox_modelSelect.addItems(self.model_manager.get_model_names())

    def model_init(self):
        # 获取当前选择的模型名称
        current_model = self.combox_modelSelect.currentText()
        
        # 如果选择为空，直接返回
        if not current_model:
            return
            
        try:
            # 初始化模型
            self.model_manager.init_model(current_model)
            # 初始化成功后显示提示
            QMessageBox.information(self, "提示", f"模型 {current_model} 初始化成功！")
            
        except Exception as e:
            # 初始化失败时显示错误信息
            QMessageBox.critical(self, "错误", f"模型初始化失败：{str(e)}")

    def closeEvent(self, event):
        #在关闭窗口时，释放资源
        self.m_flag = False
        event.accept()

    def upload_audio(self):
        # 从文件系统选择音视频文件，并显示在lab_audioname中
        file_dialog = QFileDialog()
        # 设置文件过滤器，只显示音视频文件
        file_filter = "音视频文件 (*.mp3 *.wav *.mp4 *.avi *.mkv);;所有文件 (*.*)"
        # 打开文件选择对话框
        file_path, _ = file_dialog.getOpenFileName(
            self,
            "选择音视频文件",
            "",
            file_filter
        )
        
        if file_path:
            # 保存完整文件路径
            self.audio_file_path = file_path
            # 只显示文件名
            file_name = file_path.split('/')[-1]
            self.label_audioname.setText(file_name)

    def asr(self):
        try:
            # 检查是否已选择音频文件
            if not self.audio_file_path:
                QMessageBox.warning(self, "警告", "请先选择音频文件！")
                return
            
            # 检查模型是否已初始化
            if not self.model_manager.is_model_initialized():
                QMessageBox.warning(self, "警告", "请先初始化模型！")
                return
            
            # 使用完整路径加载音频文件
            waveform, sample_rate = torchaudio.load(self.audio_file_path)
            
            # 重采样到16kHz
            if sample_rate != 16000:
                resampler = torchaudio.transforms.Resample(sample_rate, 16000)
                waveform = resampler(waveform)
            
            # 转换为单声道
            if waveform.dim() > 1:
                waveform = waveform.mean(0)
            
            # 转换为float32格式
            waveform = waveform.numpy().astype(np.float32)
            
            # 执行推理
            result = self.model_manager.inference(waveform)
            
            # 显示识别结果
            if result and len(result) > 0:
                self.txtEdit_result.setText(result[0]["text"])
            else:
                self.txtEdit_result.setText("未能识别出文本")
            
            # 清理缓存
            if hasattr(torch.cuda, 'empty_cache'):
                torch.cuda.empty_cache()
            
        except Exception as e:
            QMessageBox.critical(self, "错误", f"识别过程出错：{str(e)}")
