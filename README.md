hw04 大模型语音技术全链路作业
项目简介
本项目完成文本生成 → 声音克隆 / 文本朗读 → 语音识别全流程实验，使用大模型生成技术文稿，通过剪映生成配音音频，再基于开源 ASR 模型实现语音转文字，完成闭环验证。
任务三 安装运行说明：
安装依赖：bash
运行：pip install -r requirements.txt
安装 ffmpeg
运行语音识别：bash
运行：python asr_demo.py
查看结果：识别文本自动保存到 asr_result.txt
