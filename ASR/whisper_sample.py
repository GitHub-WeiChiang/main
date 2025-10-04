import whisper

def main(
        audio_path: str,
        output_dir: str,
        initial_prompt: str,
        language: str = "zh",
        model_size: str = "large"
):
    # 檢查模型大小是否在允許清單內
    if model_size not in ["small", "medium", "large"]:
        raise ValueError("model_size must be one of ['small', 'medium', 'large']")
    
    # 載入對應尺寸的 Whisper 模型
    model = whisper.load_model(model_size)

    # 呼叫轉錄
    result = model.transcribe(
        audio_path,
        temperature=0.1,
        fp16=False,
        language=language,
        verbose=True,
        initial_prompt=initial_prompt,
        condition_on_previous_text=False,
    )

    # 取得轉錄結果
    result_text = result["text"]

    # 輸出文字檔
    with open(output_dir, "w", encoding="utf-8") as f:
        f.write(result_text)

if __name__ == "__main__":
    prompt = "討論主題: 有關於飛彈的攔截率"

    main("./audio/test_audio.wav", "./transcript/whisper.txt", prompt)
