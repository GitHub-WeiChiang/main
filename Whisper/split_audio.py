from pydub import AudioSegment

def split_audio(input_path, output_path, start_ms, end_ms, audio_format="wav"):
    """
    將原始音檔依據指定時間範圍切割出一小段並輸出為新檔。

    input_path: 原始音檔路徑
    output_path: 輸出音檔路徑
    start_ms: 起始時間 (毫秒)
    end_ms: 結束時間 (毫秒)
    audio_format: 輸出格式
    """

    # 讀取
    audio = AudioSegment.from_file(input_path)
    # 切割
    segment = audio[start_ms:end_ms]
    # 匯出
    segment.export(output_path, format=audio_format)

if __name__ == "__main__":
    input_path = "./audio/test_audio_3.wav"
    output_path = "./segment/temp_segment_3.wav"
    
    start_ms = 0
    end_ms = 24000

    split_audio(
        input_path,
        output_path,
        start_ms=start_ms,
        end_ms=end_ms
    )

    print(f"已輸出片段：{start_ms/1000:.2f}s ~ {end_ms/1000:.2f}s -> {output_path}")
