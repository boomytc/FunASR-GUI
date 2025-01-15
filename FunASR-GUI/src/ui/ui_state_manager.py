from PySide6.QtCore import QObject, Signal

class UIStateManager_ASR(QObject):
    # 状态变更信号
    asr_controls_state_changed = Signal(bool)  # True表示启用，False表示禁用
    batch_controls_state_changed = Signal(bool)
    status_message_changed = Signal(str)
    result_text_changed = Signal(str)
    save_message_changed = Signal(str)
    batch_progress_message_changed = Signal(str)
    
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self._connect_signals()
    
    def _connect_signals(self):
        """连接信号到对应的UI更新函数"""
        self.asr_controls_state_changed.connect(self._update_asr_controls_state)
        self.batch_controls_state_changed.connect(self._update_batch_controls_state)
        self.status_message_changed.connect(self._update_status_message)
        self.result_text_changed.connect(self._update_result_text)
        self.save_message_changed.connect(self._update_save_message)
        self.batch_progress_message_changed.connect(self._update_batch_progress)
    
    def _update_asr_controls_state(self, enabled: bool):
        """更新ASR控件状态"""
        self.main_window.btn_asr.setEnabled(enabled)
        self.main_window.btn_upload_audio.setEnabled(enabled)
        self.main_window.combox_modelSelect.setEnabled(enabled)
    
    def _update_batch_controls_state(self, enabled: bool):
        """更新批量处理控件状态"""
        self.main_window.btn_batch_asr.setEnabled(enabled)
        self.main_window.btn_batch_asr_inputDir_select.setEnabled(enabled)
        self.main_window.btn_batch_asr_outputDir_select.setEnabled(enabled)
        self.main_window.combox_modelSelect_batch.setEnabled(enabled)
    
    def _update_status_message(self, message: str):
        """更新状态栏消息"""
        self.main_window.statusbar.showMessage(message)
    
    def _update_result_text(self, text: str):
        """更新结果文本"""
        self.main_window.txtEdit_result.setText(text)
    
    def _update_save_message(self, message: str):
        """更新保存消息"""
        self.main_window.lab_asrSaveMessage.setText(message)
    
    def _update_batch_progress(self, message: str):
        """更新批量处理进度"""
        self.main_window.plainTextEdit_batch_asr_result.appendPlainText(message)

    def get_ui_state(self):
        """获取当前UI状态"""
        return {
            'use_timestamp': self.main_window.radiobtn_timestampY.isChecked(),
            'distinguish_speaker': self.main_window.radiobtn_spkY.isChecked(),
            'save_mode': 'txt' if self.main_window.radioBtn_asrSaveTxtMode.isChecked() else 'srt',
            'save_directory': self.main_window.lineEdit_asrSavaDir.text(),
            'batch_input_dir': self.main_window.lineEdit_batch_asr_inputDir.text(),
            'batch_output_dir': self.main_window.lineEdit_batch_asr_outputDir.text(),
            'is_save_enabled': self.main_window.chkbox_asrResultSave.isChecked()
        } 