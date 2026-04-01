实验名称：基于OpenAI Whisper的语音识别实验
操作系统：Windows 11
Python 版本：3.10
硬件：CPU运行，无GPU
依赖库：openai-whisper、ffmpeg-python
音频文件：dub_audio.mp3（剪映文本朗读生成）
音频来源：hw04 任务一文本 + 剪映文本朗读合成
实验步骤：
安装依赖包：pip install openai-whisper
安装ffmpeg用于音频解码
编写音频识别脚本asr_demo.py
加载base模型，对dub_audio.mp3进行识别
将识别结果保存到asr_result.txt
对比原文与识别结果，记录准确率与耗时
实验结果
模型：whisper base
识别语言：中文
音频时长：约1分钟左右
识别耗时：约8秒（CPU环境）
识别结果：与原文基本一致，文字准确，仅少量标点差异
