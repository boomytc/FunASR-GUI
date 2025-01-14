from PySide6.QtWidgets import QFileDialog, QMessageBox
from utils.ffmpeg_utils import FFmpegUtils
import os
from typing import Optional, Tuple

#文件控制器，负责处理文件操作和UI交互
class FileController:
    #初始化文件控制器(parent_widget: 父级窗口部件，用于显示对话框和消息框)
    def __init__(self, parent_widget=None):
        self.parent_widget = parent_widget
        self.current_audio_path = None  # 当前处理后的音频文件路径
        self.original_filename = None   # 原始文件名

    #打开文件选择对话框并处理音频文件上传(Tuple[bool, Optional[str]]: 是否成功, 处理后的文件路径或错误信息)
    def upload_audio(self) -> Tuple[bool, Optional[str]]:
        """处理音频文件上传
        Returns:
            tuple: (是否成功, 处理后的文件路径或错误信息)
        """
        try:
            # 打开文件选择对话框
            file_path, _ = QFileDialog.getOpenFileName(
                self.parent_widget,
                "选择音频文件",
                "",
                "音频文件 (*.mp3 *.wav *.m4a *.flac *.ogg *.aac)"
            )
            
            if not file_path:
                return False, "未选择文件"

            # 保存原始文件名
            self.original_filename = os.path.basename(file_path)
            
            # 转换音频格式
            success, result = FFmpegUtils.convert_to_wav(file_path)
            
            if success:
                self.current_audio_path = result
                return True, result
            else:
                return False, result
                
        except Exception as e:
            return False, f"文件上传失败：{str(e)}"

    #获取当前处理的音频文件路径(返回值：Optional[str]: 当前音频文件路径 | None: 没有处理音频文件)
    def get_current_audio_path(self) -> Optional[str]:
        return self.current_audio_path

    #获取原始文件名(返回值：str: 原始文件名)
    def get_original_filename(self) -> str:
        return self.original_filename

    #获取文件名(file_path: 文件路径 | 返回值：str: 文件名)
    def get_file_name(self, file_path: str) -> str:
        return os.path.basename(file_path)
