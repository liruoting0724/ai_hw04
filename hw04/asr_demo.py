import whisper
model = whisper.load_model("base")
audio_path = "dub_audio.mp3"
result = model.transcribe(audio_path, language="zh")
with open("asr_result.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
print("识别完成，结果已保存到asr_result.txt")
print("识别内容：\n", result["text"])
