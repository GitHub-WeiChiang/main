import os
import whisper

from typing import List, Dict

# 把秒數轉成 mm:ss.mmm 格式
def format_timestamp(seconds: float) -> str:
    # 把秒轉成毫秒
    ms = int(round(seconds * 1000))

    # 把毫秒分成 "秒" 與 "剩餘毫秒"。
    s, ms = divmod(ms, 1000)
    # 把秒數分成 "分鐘" 與 "剩餘秒"。
    m, s = divmod(s, 60)

    # 格式化輸出
    return f"{m:02d}:{s:02d}.{ms:03d}"

# 把 segments 寫成帶時間戳的 txt 且每行一個 segment
def write_transcript_with_timestamps(segments: List[Dict], output_dir: str) -> None:
    with open(output_dir, "w", encoding="utf-8") as f:
        for seg in segments:
            start = format_timestamp(seg["start"])
            end = format_timestamp(seg["end"])

            text = seg.get("text", "").strip()
            
            f.write(f"[{start} --> {end}] {text}\n")

def main(
        audio_path: str,
        output_dir: str,
        initial_prompt: str,
        language: str = "zh",
        model_size: str = "large"
):
    print("正在進行轉錄 [", initial_prompt, "]")

    # 檢查模型大小是否在允許清單內
    if model_size not in ["tiny", "base", "small", "medium", "large"]:
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

    # 取得轉錄結果中的 segments
    segments = result.get("segments")

    # 若有 segments 輸出帶時間戳的文字檔
    if segments:
        write_transcript_with_timestamps(segments, output_dir)
    # 否則退回寫純 text
    else:
        # 取得轉錄結果
        result_text = result["text"]

        # 輸出文字檔
        with open(output_dir, "w", encoding="utf-8") as f:
            f.write(result_text)

if __name__ == "__main__":
    os.makedirs("./model", exist_ok=True)
    
    os.environ["XDG_CACHE_HOME"] = "./model"

    prompt = "討論主題: 有關於飛彈的攔截率"
    main("./audio/test_audio_1.wav", "./transcript/whisper_1.txt", prompt)

    prompt = "討論主題: 有關於法令紋與肉毒"
    main("./audio/test_audio_2.wav", "./transcript/whisper_2.txt", prompt)

    prompt = "討論主題: 有關於人生的意義"
    main("./audio/test_audio_3.wav", "./transcript/whisper_3.txt", prompt)
