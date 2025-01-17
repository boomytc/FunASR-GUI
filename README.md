# FunASR-GUI

基于 FunASR 的语音识别图形界面工具，支持语音识别、语音合成和音视频处理功能。

## 功能特点

- 语音识别
  - 单文件识别
  - 批量文件识别
  - 支持时间戳和说话人区分
  - 支持 TXT 和 SRT 格式导出
- 语音合成 (开发中，CosyVoice太难集成，准备新开个项目)
- 音视频处理 (开发中)
- 模型对比功能 (开发中)

## 支持的模型(modelscope上的Paraformer模型)

- Paraformer语音识别-中文-通用-16k-离线-large-长音频版模型

## 环境要求

- Python 3.10
- FFmpeg
- CUDA (可选，用于GPU加速)

## 安装说明

1. 克隆项目
```bash
git clone https://github.com/yourusername/FunASR-GUI.git && cd FunASR-GUI
```
2. 创建虚拟环境
```bash
python -m venv .venv
source .venv/bin/activate # Linux/macOS
或
.venv\Scripts\activate # Windows
```
3. 安装依赖
```bash
pip install torch torchvision torchaudio
pip install PySide6
pip install -U funasr
```

4. 配置模型路径
编辑 `config.ini` 文件，设置正确的模型路径：
```ini
[ASRModelPaths]
Linux/macOS
base_dir = /path/to/your/models
Windows
#base_dir = C:/path/to/your/models
```

## 使用说明

1. 启动程序
```bash 
python src/main.py
```

2. 语音识别使用流程：
   - 选择识别模型
   - 上传音频文件
   - 配置识别参数（时间戳、说话人区分等）
   - 点击"开始识别"
   - 查看识别结果
   - 保存结果（支持TXT和SRT格式）

## 项目结构
```markdownkdown
FunASR-GUI/
├── config.ini        # 配置文件
├── src/              # 源代码目录
│   ├── main.py       # 程序入口
│   ├── MainProcess.py  # 主窗口处理
│   ├── asr_process.py  # 语音识别处理
│   ├── controllers/  # 控制器
│   ├── services/     # 服务层
│   ├── ui/           # UI文件
│   ├── utils/        # 工具类
│   └── models/       # 模型目录
```

## 注意事项

1. 首次使用需要下载相应的模型文件
2. 确保系统已安装FFmpeg
3. 建议使用GPU进行识别，可大幅提升处理速度
4. 批量处理大量文件时注意系统资源占用

## 许可证

[出来混的要什么许可，直接开源]

## 贡献指南

欢迎提交Issue和Pull Request，但是我只会git push，其他的不会看也不会用，所以请自行解决。

## 致谢

- [FunASR](https://github.com/alibaba-damo-academy/FunASR)
- [FFmpeg](https://ffmpeg.org/)
