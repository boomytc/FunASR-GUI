import subprocess
import os
from typing import Tuple, Optional
import logging
import atexit
import time

#FFmpeg 工具类，用于音视频文件处理
class FFmpegUtils:
    # 类变量，用于跟踪所有临时文件
    _temp_files = set()

    @staticmethod
    def _add_temp_file(file_path: str):
        """添加临时文件到跟踪列表"""
        FFmpegUtils._temp_files.add(file_path)

    @staticmethod
    def _cleanup_temp_files():
        """清理所有临时文件"""
        for file_path in FFmpegUtils._temp_files:
            try:
                if os.path.exists(file_path):
                    os.remove(file_path)
            except Exception as e:
                logging.warning(f"清理临时文件失败 {file_path}: {str(e)}")
        FFmpegUtils._temp_files.clear()

    #检查系统是否安装了 FFmpeg(bool: FFmpeg 是否可用)
    @staticmethod
    def check_ffmpeg_installed() -> bool:
        try:
            subprocess.run(['ffmpeg', '-version'], capture_output=True)
            return True
        except FileNotFoundError:
            return False

    #将音视频文件转换为指定采样率和声道数的 WAV 文件(input_path: 输入文件路径 | output_path: 输出文件路径 | sample_rate: 采样率 | channels: 声道数 | Tuple[bool, str]: 转换结果[是否成功, 输出文件路径或错误信息])
    @staticmethod
    def convert_to_wav(
        input_path: str,
        output_path: Optional[str] = None,
        sample_rate: int = 16000,
        channels: int = 1   #声道数
    ) -> Tuple[bool, str]:

        try:
            if not os.path.exists(input_path):
                return False, f"输入文件不存在: {input_path}"
            
            if not FFmpegUtils.check_ffmpeg_installed():
                return False, "未安装 FFmpeg，请先安装 FFmpeg"
            
            # 如果未指定输出路径，则在原文件同目录下创建临时文件
            if output_path is None:
                directory = os.path.dirname(input_path)
                filename = os.path.splitext(os.path.basename(input_path))[0]
                output_path = os.path.join(directory, f"{filename}_temp_{int(time.time())}.wav")
                # 将生成的临时文件添加到跟踪列表
                FFmpegUtils._add_temp_file(output_path)
            
            # 构建 FFmpeg 命令
            command = [
                'ffmpeg',
                '-i', input_path,
                '-ar', str(sample_rate),
                '-ac', str(channels),
                '-y',  # 覆盖已存在的文件
                output_path
            ]
            
            # 执行转换
            process = subprocess.run(
                command,
                capture_output=True,
                text=True
            )
            
            if process.returncode != 0:
                return False, f"转换失败: {process.stderr}"
            
            return True, output_path
            
        except Exception as e:
            return False, f"转换过程出错: {str(e)}"

    #获取音频文件的基本信息(file_path: 音频文件路径 | Tuple[bool, dict]: 获取结果[是否成功, 包含音频信息的字典或错误信息])
    @staticmethod
    def get_audio_info(file_path: str) -> Tuple[bool, dict]:
        try:
            if not os.path.exists(file_path):
                return False, {"error": "文件不存在"}
                
            command = [
                'ffprobe',
                '-v', 'quiet',
                '-print_format', 'json',
                '-show_format',
                '-show_streams',
                file_path
            ]
            
            process = subprocess.run(
                command,
                capture_output=True,
                text=True
            )
            
            if process.returncode != 0:
                return False, {"error": "获取音频信息失败"}
                
            import json
            info = json.loads(process.stdout)
            
            # 提取关键信息
            audio_info = {
                "format": info.get("format", {}).get("format_name", "unknown"),
                "duration": float(info.get("format", {}).get("duration", 0)),
                "size": int(info.get("format", {}).get("size", 0))
            }
            
            # 查找音频流信息
            for stream in info.get("streams", []):
                if stream.get("codec_type") == "audio":
                    audio_info.update({
                        "sample_rate": int(stream.get("sample_rate", 0)),
                        "channels": int(stream.get("channels", 0)),
                        "codec": stream.get("codec_name", "unknown")
                    })
                    break
                    
            return True, audio_info
            
        except Exception as e:
            return False, {"error": f"处理过程出错: {str(e)}"}

# 注册程序退出时的清理函数
atexit.register(FFmpegUtils._cleanup_temp_files)


