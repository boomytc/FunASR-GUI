from PySide6.QtWidgets import QFileDialog, QMessageBox
from utils.ffmpeg_utils import FFmpegUtils
import os
from typing import Optional, Tuple
import sys

#文件控制器，负责处理文件操作和UI交互
class FileController:
    #初始化文件控制器(parent_widget: 父级窗口部件，用于显示对话框和消息框)
    def __init__(self, parent_widget=None):
        self.parent_widget = parent_widget
        self.ui_state_manager = parent_widget.ui_state_manager if parent_widget else None
        self.current_audio_path = None  # 当前处理后的音频文件路径
        self.original_filename = None   # 原始文件名

    #打开文件选择对话框并处理音频文件上传(Tuple[bool, Optional[str]]: 是否成功, 处理后的文件路径或错误信息)
    def upload_audio(self) -> Tuple[bool, Optional[str]]:
        try:
            # 打开文件选择对话框
            file_path, _ = QFileDialog.getOpenFileName(
                self.ui_state_manager.main_window if self.ui_state_manager else None,
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
    
    #选择ASR结果保存目录
    def select_asr_result_dir(self):
        pass
    
    def save_asr_result(self, result: str, save_dir: str, save_mode: str, base_name: str = None) -> Tuple[bool, str]:
        """保存识别结果到指定目录
        Args:
            result: 识别结果文本
            save_dir: 保存目录
            save_mode: 保存模式 ('txt' 或 'srt')
            base_name: 指定的文件名（不含扩展名），如果为None则使用原始文件名
        Returns:
            tuple[bool, str]: 是否成功, 成功或错误信息
        """
        try:
            if not base_name and not self.original_filename:
                return False, "没有原始文件名信息"
            
            if not os.path.exists(save_dir):
                return False, "保存目录不存在"
            
            # 获取文件名（不含扩展名）
            file_base_name = base_name if base_name else os.path.splitext(self.original_filename)[0]
            
            # 根据保存模式设置文件扩展名和处理内容
            if save_mode == 'txt':
                # 处理纯文本模式：移除时间戳和说话人信息
                lines = result.split('\n')
                text_only = []
                for line in lines:
                    # 跳过时间戳行（包含 --> 的行）
                    if '-->' in line:
                        continue
                    # 跳过字幕序号行（纯数字的行）
                    if line.strip().isdigit():
                        continue
                    # 跳过空行
                    if not line.strip():
                        continue
                    # 移除说话人标识 [spkX]
                    if line.strip().startswith('[spk'):
                        line = line[line.find(']')+1:].strip()
                    text_only.append(line)
                
                content = '\n'.join(text_only)
                file_path = os.path.join(save_dir, f"{file_base_name}.txt")
                
            elif save_mode == 'srt':
                # SRT模式：直接使用完整结果
                content = result
                file_path = os.path.join(save_dir, f"{file_base_name}.srt")
                
            else:
                return False, "无效的保存模式"
            
            # 保存文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True, file_path
        
        except Exception as e:
            return False, f"保存失败：{str(e)}"


    #选择ASR结果保存目录(current_dir: 当前设置的目录路径 | 返回值：tuple[bool, str]: 是否成功选择了新目录, 选择的目录路径或保持原有路径)
    def select_asr_save_directory(self, current_dir: str = "") -> Tuple[bool, str]:
        try:
            # 如果没有指定当前目录，优先使用上传音频所在目录
            default_dir = current_dir
            if not default_dir and self.current_audio_path:
                default_dir = os.path.dirname(self.current_audio_path)
            elif not default_dir:
                default_dir = os.path.expanduser('~')  # 如果没有音频文件，则使用用户主目录
            
            # 打开目录选择对话框
            save_dir = QFileDialog.getExistingDirectory(
                self.ui_state_manager.main_window if self.ui_state_manager else None,
                "选择保存目录",
                default_dir
            )
            
            # 如果用户选择了目录（而不是取消）
            if save_dir:
                return True, save_dir
            # 如果取消选择，优先返回音频所在目录
            if self.current_audio_path:
                return True, os.path.dirname(self.current_audio_path)
            return False, current_dir
                
        except Exception as e:
            return False, f"选择目录失败：{str(e)}"

    def open_asr_save_directory(self, target_dir: str = None) -> Tuple[bool, str]:
        """打开指定目录
        Args:
            target_dir: 要打开的目录路径，如果为None则使用当前音频文件目录
        Returns:
            Tuple[bool, str]: (是否成功, 错误信息)
        """
        try:
            # 如果没有指定目录，但有音频文件，则使用音频文件所在目录
            if not target_dir and self.current_audio_path:
                target_dir = os.path.dirname(self.current_audio_path)
            
            # 检查目录是否存在
            if target_dir and os.path.exists(target_dir):
                # 根据操作系统使用不同的打开命令
                if sys.platform == 'win32':
                    os.startfile(target_dir)
                elif sys.platform == 'darwin':  # macOS
                    os.system(f'open "{target_dir}"')
                else:  # Linux
                    os.system(f'xdg-open "{target_dir}"')
                return True, ""
            else:
                return False, "目录不存在"
            
        except Exception as e:
            return False, f"无法打开目录：{str(e)}"

    def get_default_save_directory(self) -> str:
        """获取默认保存目录"""
        if self.current_audio_path:
            return os.path.dirname(self.current_audio_path)
        return os.path.expanduser('~')  # 如果没有音频文件，返回用户主目录

    def cleanup(self):
        """清理临时文件"""
        FFmpegUtils._cleanup_temp_files()

    def process_audio_file(self, audio_file: str) -> Tuple[bool, Optional[str]]:
        """处理单个音频文件
        Returns:
            Tuple[bool, str]: (是否成功, 处理后的文件路径或错误信息)
        """
        try:
            success, result = FFmpegUtils.convert_to_wav(audio_file)
            if success:
                return True, result
            return False, result
        except Exception as e:
            return False, f"音频处理失败：{str(e)}"

    def get_audio_files_in_directory(self, directory: str) -> list:
        """获取目录中的所有支持的音频文件
        Returns:
            list: 音频文件路径列表
        """
        audio_files = []
        for file in os.listdir(directory):
            if file.lower().endswith(('.mp3', '.wav', '.m4a', '.flac', '.ogg', '.aac')):
                audio_files.append(os.path.join(directory, file))
        return audio_files

    def cleanup_temp_file(self):
        """清理临时文件"""
        FFmpegUtils._cleanup_temp_files()