from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import QObject, Signal
import os
from controllers.model_controller import ASRModelController
from controllers.file_controller import FileController

class ASRProcess(QObject):
    # 定义信号
    error_occurred = Signal(str, str)  # (title, message)
    warning_occurred = Signal(str, str)
    
    def __init__(self, ui_state_manager):
        super().__init__()
        self.ui_state_manager = ui_state_manager
        
        # 创建控制器实例
        self.model_controller = ASRModelController(self)
        self.file_controller = FileController(self)
        
        # 批量处理的目录缓存
        self.batch_input_dir = ""
        self.batch_output_dir = ""
        
        # 连接错误信号
        self.error_occurred.connect(self._show_error_message)
        self.warning_occurred.connect(self._show_warning_message)
        
        # 设置ComboBox
        self.setup_model_combobox()
        
        # 连接保存模式变化信号
        ui = self.ui_state_manager.main_window
        ui.radioBtn_asrSaveSrtMode.toggled.connect(self._handle_srt_mode_change)
        ui.radioBtn_batch_asrSaveSrtMode.toggled.connect(self._handle_batch_srt_mode_change)
        ui.radioBtn_asrSaveTxtMode.toggled.connect(self._handle_txt_mode_change)
        ui.radioBtn_batch_asrSaveTxtMode.toggled.connect(self._handle_batch_txt_mode_change)

    def _show_error_message(self, title: str, message: str):
        """显示错误消息"""
        self.ui_state_manager.status_message_changed.emit(message)
        
    def _show_warning_message(self, title: str, message: str):
        """显示警告消息"""
        self.ui_state_manager.status_message_changed.emit(message)
        
    def setup_model_combobox(self):
        """设置模型ComboBox"""
        model_names = self.model_controller.get_model_names()
        ui = self.ui_state_manager.main_window
        
        ui.combox_modelSelect.clear()
        ui.combox_modelSelect_batch.clear()
        
        default_text = "请选择语音识别模型"
        ui.combox_modelSelect.addItem(default_text)
        ui.combox_modelSelect_batch.addItem(default_text)
        
        ui.combox_modelSelect.addItems(model_names)
        ui.combox_modelSelect_batch.addItems(model_names)

    def model_init_single(self, index):
        """单文件处理的模型初始化"""
        current_model = self.ui_state_manager.main_window.combox_modelSelect.currentText()
        self.model_controller.initialize_model(current_model)

    def model_init_batch(self, index):
        """批处理的模型初始化"""
        current_model = self.ui_state_manager.main_window.combox_modelSelect_batch.currentText()
        self.model_controller.initialize_model(current_model)

    def upload_audio(self):
        """处理音频文件上传"""
        success, result = self.file_controller.upload_audio()
        if success:
            self.audio_file_path = result
            original_filename = self.file_controller.get_original_filename()
            self.ui_state_manager.main_window.label_audioname.setText(original_filename)
        else:
            self.error_occurred.emit("错误", result)

    def asr_result_save_state(self):
        """ASR结果保存开启状态"""
        ui = self.ui_state_manager.main_window
        if ui.chkbox_asrResultSave.isChecked():
            ui.groupBox_asrSave.setEnabled(True)
            if not ui.lineEdit_asrSavaDir.text():
                default_dir = self.file_controller.get_default_save_directory()
                ui.lineEdit_asrSavaDir.setText(default_dir)
        else:
            ui.groupBox_asrSave.setEnabled(False)

    def select_asr_result_dir(self):
        """选择ASR结果保存目录"""
        current_dir = self.ui_state_manager.main_window.lineEdit_asrSavaDir.text()
        success, result = self.file_controller.select_asr_save_directory(current_dir)
        
        if success:
            self.ui_state_manager.main_window.lineEdit_asrSavaDir.setText(result)
        elif not isinstance(result, str):
            self.error_occurred.emit("错误", result)

    def open_asr_result_dir(self):
        """打开ASR结果保存目录"""
        target_dir = self.ui_state_manager.main_window.lineEdit_asrSavaDir.text()
        success, error_msg = self.file_controller.open_asr_save_directory(target_dir)
        
        if not success:
            self.error_occurred.emit("错误", error_msg)

    def asr(self):
        """语音识别处理"""
        if not self.file_controller.get_current_audio_path():
            self.warning_occurred.emit("警告", "请先选择音频文件！")
            return
        
        ui_state = self.ui_state_manager.get_ui_state()
        success, thread_or_error = self.model_controller.perform_asr(
            self.audio_file_path,
            use_timestamp=ui_state['use_timestamp'],
            distinguish_speaker=ui_state['distinguish_speaker']
        )
        
        if not success:
            self.error_occurred.emit("错误", thread_or_error)
            return

        self.ui_state_manager.asr_controls_state_changed.emit(False)
        
        asr_thread = thread_or_error
        asr_thread.progress.connect(
            lambda msg: self.ui_state_manager.status_message_changed.emit(msg)
        )
        asr_thread.finished.connect(self._on_asr_finished)
        asr_thread.start()

    def _on_asr_finished(self, success, result):
        """ASR完成回调"""
        if success:
            self.ui_state_manager.result_text_changed.emit(result)
            
            ui_state = self.ui_state_manager.get_ui_state()
            if ui_state['is_save_enabled']:
                save_success, save_path = self.file_controller.save_asr_result(
                    result,
                    ui_state['save_directory'],
                    ui_state['save_mode']
                )
                
                save_message = (
                    f"成功保存 {os.path.basename(save_path)}" if save_success 
                    else f"保存失败：{save_path}"
                )
                self.ui_state_manager.save_message_changed.emit(save_message)
        else:
            self.error_occurred.emit("错误", result)
        
        self.ui_state_manager.asr_controls_state_changed.emit(True)
        self.ui_state_manager.status_message_changed.emit("识别完成")

    def clear_asr(self):
        """清除语音识别结果"""
        self.ui_state_manager.result_text_changed.emit("")

    def select_batch_input_dir(self):
        """选择批量处理的输入目录"""
        current_dir = self.ui_state_manager.main_window.lineEdit_batch_asr_inputDir.text()
        success, result = self.file_controller.select_asr_save_directory(current_dir)
        
        if success:
            self.ui_state_manager.main_window.lineEdit_batch_asr_inputDir.setText(result)
        elif not isinstance(result, str):
            self.error_occurred.emit("错误", result)

    def select_batch_output_dir(self):
        """选择批量处理的输出目录"""
        current_dir = self.ui_state_manager.main_window.lineEdit_batch_asr_inputDir.text()
        success, result = self.file_controller.select_asr_save_directory(current_dir)
        
        if success:
            self.ui_state_manager.main_window.lineEdit_batch_asr_outputDir.setText(result)
        elif not isinstance(result, str):
            self.error_occurred.emit("错误", result)

    def open_batch_input_dir(self):
        """打开批量处理的输入目录"""
        target_dir = self.ui_state_manager.main_window.lineEdit_batch_asr_inputDir.text()
        success, error_msg = self.file_controller.open_asr_save_directory(target_dir)
        
        if not success:
            self.error_occurred.emit("错误", error_msg)

    def open_batch_output_dir(self):
        """打开批量处理的输出目录"""
        target_dir = self.ui_state_manager.main_window.lineEdit_batch_asr_outputDir.text()
        success, error_msg = self.file_controller.open_asr_save_directory(target_dir)
        
        if not success:
            self.error_occurred.emit("错误", error_msg)

    def batch_asr(self):
        """批量处理语音识别"""
        ui_state = self.ui_state_manager.get_ui_state()
        input_dir = ui_state['batch_input_dir']
        output_dir = ui_state['batch_output_dir']
        
        if not input_dir or not os.path.exists(input_dir):
            self.ui_state_manager.batch_progress_message_changed.emit("错误：请选择有效的输入目录！")
            return
        if not output_dir or not os.path.exists(output_dir):
            self.ui_state_manager.batch_progress_message_changed.emit("错误：请选择有效的输出目录！")
            return
        
        audio_files = self.file_controller.get_audio_files_in_directory(input_dir)
        if not audio_files:
            self.ui_state_manager.batch_progress_message_changed.emit("错误：输入目录中没有找到支持的音频文件！")
            return
        
        success, thread_or_error = self.model_controller.perform_batch_asr(
            audio_files,
            use_timestamp=ui_state['use_timestamp'],
            distinguish_speaker=ui_state['distinguish_speaker']
        )
        
        if not success:
            self.ui_state_manager.batch_progress_message_changed.emit(f"错误：{thread_or_error}")
            return

        self.ui_state_manager.batch_progress_message_changed.emit("开始处理音频文件...\n")
        self.ui_state_manager.batch_controls_state_changed.emit(False)
        
        batch_thread = thread_or_error
        batch_thread.progress.connect(self._update_batch_progress)
        batch_thread.file_finished.connect(self._on_batch_file_finished)
        batch_thread.finished.connect(self._on_batch_asr_finished)
        batch_thread.start()

    def _update_batch_progress(self, message):
        """更新批量处理进度"""
        self.ui_state_manager.status_message_changed.emit(message)
        self.ui_state_manager.batch_progress_message_changed.emit(message)

    def _on_batch_file_finished(self, success, file_name, result):
        """批量处理单个文件完成回调"""
        ui_state = self.ui_state_manager.get_ui_state()
        save_mode = ui_state['save_mode']
        output_dir = ui_state['batch_output_dir']
        
        if success:
            save_success, save_msg = self.file_controller.save_asr_result(
                result,
                output_dir,
                save_mode,
                os.path.splitext(file_name)[0]
            )
            status = "✓" if save_success else "✘"
            message = f"{status} {file_name}: {'处理成功' if save_success else save_msg}"
        else:
            message = f"✘ {file_name}: {result}"
        
        self.ui_state_manager.batch_progress_message_changed.emit(message)

    def _on_batch_asr_finished(self):
        """批量处理完成回调"""
        self.ui_state_manager.batch_controls_state_changed.emit(True)
        self.ui_state_manager.status_message_changed.emit("批量处理完成")
        self.ui_state_manager.batch_progress_message_changed.emit("\n批量处理完成！")

    def _handle_srt_mode_change(self, checked):
        """处理单文件SRT保存模式变化"""
        ui = self.ui_state_manager.main_window
        if checked:
            ui.radiobtn_timestampY.setChecked(True)
            ui.radiobtn_timestampN.setEnabled(False)
        else:
            ui.radiobtn_timestampN.setEnabled(True)

    def _handle_batch_srt_mode_change(self, checked):
        """处理批处理SRT保存模式变化"""
        ui = self.ui_state_manager.main_window
        if checked:
            ui.radiobtn_timestampY_batch_asr.setChecked(True)
            ui.radiobtn_timestampN_batch_asr.setEnabled(False)
        else:
            ui.radiobtn_timestampN_batch_asr.setEnabled(True)

    def _handle_txt_mode_change(self, checked):
        """处理单文件TXT保存模式变化"""
        ui = self.ui_state_manager.main_window
        if checked:
            ui.radiobtn_timestampN.setChecked(True)
            ui.radiobtn_timestampY.setEnabled(False)
            ui.radiobtn_spkN.setChecked(True)
            ui.radiobtn_spkY.setEnabled(False)
        else:
            ui.radiobtn_timestampY.setEnabled(True)
            ui.radiobtn_spkY.setEnabled(True)

    def _handle_batch_txt_mode_change(self, checked):
        """处理批处理TXT保存模式变化"""
        ui = self.ui_state_manager.main_window
        if checked:
            ui.radiobtn_timestampN_batch_asr.setChecked(True)
            ui.radiobtn_timestampY_batch_asr.setEnabled(False)
            ui.radiobtn_spkN_batch_asr.setChecked(True)
            ui.radiobtn_spkY_batch_asr.setEnabled(False)
        else:
            ui.radiobtn_timestampY_batch_asr.setEnabled(True)
            ui.radiobtn_spkY_batch_asr.setEnabled(True)