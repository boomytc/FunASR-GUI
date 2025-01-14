from PySide6.QtWidgets import QWidget, QMessageBox
import os
from controllers.model_controller import ASRModelController
from controllers.file_controller import FileController
from utils.ffmpeg_utils import FFmpegUtils

class ASRProcess(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 获取父窗口中的UI元素
        self.ui = parent
        self.setup_ui_elements()
        
        # 创建控制器实例
        self.model_controller = ASRModelController(self)
        self.file_controller = FileController(self)
        
        # 批量处理的目录缓存
        self.batch_input_dir = ""
        self.batch_output_dir = ""
        
        # 设置ComboBox
        self.setup_model_combobox()
        
        # 连接信号
        self.connect_signals()
        
    def setup_ui_elements(self):
        """获取需要的UI元素引用"""
        self.combox_modelSelect = self.ui.combox_modelSelect
        self.btn_upload_audio = self.ui.btn_upload_audio
        self.btn_asr = self.ui.btn_asr
        self.btn_asr_clear = self.ui.btn_asr_clear
        self.btn_asrResultDirSelect = self.ui.btn_asrResultDirSelect
        self.chkbox_asrResultSave = self.ui.chkbox_asrResultSave
        self.btn_asrResultDirOpen = self.ui.btn_asrResultDirOpen
        self.label_audioname = self.ui.label_audioname
        self.lineEdit_asrSavaDir = self.ui.lineEdit_asrSavaDir
        self.groupBox_asrSave = self.ui.groupBox_asrSave
        self.txtEdit_result = self.ui.txtEdit_result
        self.lab_asrSaveMessage = self.ui.lab_asrSaveMessage
        self.radiobtn_timestampY = self.ui.radiobtn_timestampY
        self.radiobtn_spkY = self.ui.radiobtn_spkY
        self.radioBtn_asrSaveTxtMode = self.ui.radioBtn_asrSaveTxtMode   
        self.combox_modelSelect_batch = self.ui.combox_modelSelect_batch
        self.btn_batch_asr_inputDir_select = self.ui.btn_batch_asr_inputDir_select
        self.btn_batch_asr_outputDir_select = self.ui.btn_batch_asr_outputDir_select
        self.btn_batch_asr_inputDir_open = self.ui.btn_batch_asr_inputDir_open
        self.lineEdit_batch_asr_inputDir = self.ui.lineEdit_batch_asr_inputDir
        self.lineEdit_batch_asr_outputDir = self.ui.lineEdit_batch_asr_outputDir
        self.btn_batch_asr_outputDir_open = self.ui.btn_batch_asr_outputDir_open
        self.btn_batch_asr = self.ui.btn_batch_asr
        self.radioBtn_batch_asrSaveTxtMode = self.ui.radioBtn_batch_asrSaveTxtMode
        self.radioBtn_batch_asrSaveSrtMode = self.ui.radioBtn_batch_asrSaveSrtMode
        self.radiobtn_timestampY_batch_asr = self.ui.radiobtn_timestampY_batch_asr
        self.radiobtn_spkY_batch_asr = self.ui.radiobtn_spkY_batch_asr
        self.plainTextEdit_batch_asr_result = self.ui.plainTextEdit_batch_asr_result
        self.statusbar = self.ui.statusbar

    def connect_signals(self):
        """连接所有信号槽"""
        # 为每个 ComboBox 连接到不同的初始化方法
        self.combox_modelSelect.currentIndexChanged.connect(self.model_init_single)
        self.combox_modelSelect_batch.currentIndexChanged.connect(self.model_init_batch)
        
        self.btn_upload_audio.clicked.connect(self.upload_audio)
        self.btn_asr.clicked.connect(self.asr)
        self.btn_asr_clear.clicked.connect(self.clear_asr)
        self.btn_asrResultDirSelect.clicked.connect(self.select_asr_result_dir)
        self.chkbox_asrResultSave.stateChanged.connect(self.asr_result_save_state)
        self.btn_asrResultDirOpen.clicked.connect(self.open_asr_result_dir)

        self.btn_batch_asr_inputDir_select.clicked.connect(self.select_batch_input_dir)
        self.btn_batch_asr_outputDir_select.clicked.connect(self.select_batch_output_dir)
        self.btn_batch_asr_inputDir_open.clicked.connect(self.open_batch_input_dir)
        self.btn_batch_asr_outputDir_open.clicked.connect(self.open_batch_output_dir)
        self.btn_batch_asr.clicked.connect(self.batch_asr)
        

    #设置模型ComboBox
    def setup_model_combobox(self):
        """设置模型ComboBox"""
        # 清空ComboBox
        self.combox_modelSelect.clear()
        self.combox_modelSelect_batch.clear()
        
        # 添加默认选项
        default_text = "请选择语音识别模型"
        self.combox_modelSelect.addItem(default_text)
        self.combox_modelSelect_batch.addItem(default_text)
        
        # 从控制器获取模型列表
        model_names = self.model_controller.get_model_names()
        self.combox_modelSelect.addItems(model_names)
        self.combox_modelSelect_batch.addItems(model_names)

    def model_init_single(self, index):
        """单文件处理的模型初始化"""
        current_model = self.combox_modelSelect.currentText()
        self.model_controller.initialize_model(current_model)

    def model_init_batch(self, index):
        """批处理的模型初始化"""
        current_model = self.combox_modelSelect_batch.currentText()
        self.model_controller.initialize_model(current_model)

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

    def select_batch_input_dir(self):
        """选择批量处理的输入目录"""
        current_dir = self.lineEdit_batch_asr_inputDir.text()
        success, result = self.file_controller.select_asr_save_directory(current_dir)
        
        if success:
            self.lineEdit_batch_asr_inputDir.setText(result)
        elif not isinstance(result, str):
            QMessageBox.critical(self, "错误", result)

    def select_batch_output_dir(self):
        """选择批量处理的输出目录"""
        current_dir = self.lineEdit_batch_asr_inputDir.text()
        success, result = self.file_controller.select_asr_save_directory(current_dir)
        
        if success:
            self.lineEdit_batch_asr_outputDir.setText(result)
        elif not isinstance(result, str):
            QMessageBox.critical(self, "错误", result)

    def open_batch_input_dir(self):
        """打开批量处理的输入目录"""
        target_dir = self.lineEdit_batch_asr_inputDir.text()
        success, error_msg = self.file_controller.open_asr_save_directory(target_dir)
        
        if not success:
            QMessageBox.critical(self, "错误", error_msg)

    def open_batch_output_dir(self):
        """打开批量处理的输出目录"""
        target_dir = self.lineEdit_batch_asr_outputDir.text()
        success, error_msg = self.file_controller.open_asr_save_directory(target_dir)
        
        if not success:
            QMessageBox.critical(self, "错误", error_msg)

    def batch_asr(self):
        """批量处理语音识别"""
        input_dir = self.lineEdit_batch_asr_inputDir.text()
        output_dir = self.lineEdit_batch_asr_outputDir.text()
        
        # 检查目录是否存在
        if not input_dir or not os.path.exists(input_dir):
            self.plainTextEdit_batch_asr_result.setPlainText("错误：请选择有效的输入目录！")
            return
        if not output_dir or not os.path.exists(output_dir):
            self.plainTextEdit_batch_asr_result.setPlainText("错误：请选择有效的输出目录！")
            return
        
        # 获取音频文件列表
        audio_files = self.file_controller.get_audio_files_in_directory(input_dir)
        if not audio_files:
            self.plainTextEdit_batch_asr_result.setPlainText("错误：输入目录中没有找到支持的音频文件！")
            return
        
        # 获取保存模式和设置
        save_mode = 'txt' if self.radioBtn_batch_asrSaveTxtMode.isChecked() else 'srt'
        use_timestamp = self.radiobtn_timestampY_batch_asr.isChecked()
        distinguish_speaker = self.radiobtn_spkY_batch_asr.isChecked()
        
        # 初始化进度显示
        self.plainTextEdit_batch_asr_result.clear()
        self.plainTextEdit_batch_asr_result.appendPlainText("开始处理音频文件...\n")
        
        # 处理每个音频文件
        processed_count = 0
        failed_files = []
        total_files = len(audio_files)
        
        # 初始化状态栏
        self.statusbar.showMessage("准备开始处理...")
        
        for index, audio_file in enumerate(audio_files, 1):
            file_name = os.path.basename(audio_file)
            # 更新状态栏进度
            progress = (index / total_files) * 100
            self.statusbar.showMessage(f"正在处理: {file_name} | 进度: {progress:.1f}% ({index}/{total_files})")
            
            self.plainTextEdit_batch_asr_result.appendPlainText(f"正在处理 ({index}/{total_files}): {file_name}")
            
            try:
                # 处理音频文件
                success, converted_file = self.file_controller.process_audio_file(audio_file)
                if not success:
                    error_msg = f"✘ {file_name}: 音频转换失败"
                    failed_files.append((file_name, "音频转换失败"))
                    self.plainTextEdit_batch_asr_result.appendPlainText(error_msg)
                    continue
                
                # 执行语音识别
                success, result = self.model_controller.perform_asr(
                    converted_file,
                    use_timestamp=use_timestamp,
                    distinguish_speaker=distinguish_speaker
                )
                
                if success:
                    # 保存识别结果
                    base_name = os.path.splitext(file_name)[0]
                    save_success, save_msg = self.file_controller.save_asr_result(
                        result, 
                        output_dir,
                        save_mode,
                        base_name
                    )
                    
                    if save_success:
                        processed_count += 1
                        self.plainTextEdit_batch_asr_result.appendPlainText(f"✓ {file_name}: 处理成功")
                    else:
                        error_msg = f"✘ {file_name}: 保存失败 - {save_msg}"
                        failed_files.append((file_name, f"保存失败：{save_msg}"))
                        self.plainTextEdit_batch_asr_result.appendPlainText(error_msg)
                else:
                    error_msg = f"✘ {file_name}: 识别失败 - {result}"
                    failed_files.append((file_name, f"识别失败：{result}"))
                    self.plainTextEdit_batch_asr_result.appendPlainText(error_msg)
                
            except Exception as e:
                error_msg = f"✘ {file_name}: 处理异常 - {str(e)}"
                failed_files.append((file_name, f"处理异常：{str(e)}"))
                self.plainTextEdit_batch_asr_result.appendPlainText(error_msg)
            
            finally:
                # 清理临时文件
                self.file_controller.cleanup_temp_file()
                self.plainTextEdit_batch_asr_result.appendPlainText("")  # 添加空行
        
        # 显示处理结果摘要
        summary = f"\n处理完成！\n成功处理：{processed_count}/{total_files} 个文件"
        if failed_files:
            summary += "\n\n失败文件列表："
            for file, error in failed_files:
                summary += f"\n{file}: {error}"
        
        self.plainTextEdit_batch_asr_result.appendPlainText(summary)
        
        # 更新最终状态
        success_rate = (processed_count / total_files) * 100
        self.statusbar.showMessage(f"处理完成 | 成功率: {success_rate:.1f}% ({processed_count}/{total_files})")
