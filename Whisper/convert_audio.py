import subprocess
import json

from pydub import AudioSegment

def probe_format(src):
    # 呼叫 ffprobe
    # 相當於在終端機執行
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-print_format", "json",
        "-show_format", "-show_streams", src
    ])

    # 解析 JSON 資料
    info = json.loads(out)
    fmt = info["format"]["format_name"]

    # 對映成 pydub 可用的格式名稱
    if any(k in fmt for k in ["mp4", "m4a", "mov"]):
        return "m4a"
    if "mp3" in fmt:
        return "mp3"
    if "ogg" in fmt:
        return "ogg"
    
    return None

def convert_to_wav(src, dst, ch=1, sr=16000):
    # 偵測來源格式
    fmt = probe_format(src)

    # 設定 ffmpeg 探測參數
    # "-analyzeduration", "200M": 允許 ffmpeg 多讀一些時間來判斷格式 (防止前段雜訊導致誤判)
    # "-probesize", "200M": 增加探測大小上限 (預設太小可能導致判斷失敗)
    kwargs = dict(parameters=["-analyzeduration", "200M", "-probesize", "200M"])

    # 用 pydub 讀取音訊
    # 明確指定格式
    if fmt:
        audio = AudioSegment.from_file(src, format=fmt, **kwargs)
    # 讓 ffmpeg 猜猜猜
    else:
        audio = AudioSegment.from_file(src, **kwargs)

    # 調整聲道與取樣率
    # 1: 單聲道
    # 16000: 取樣率 16kHz
    audio = audio.set_channels(ch).set_frame_rate(sr)

    # 匯出成 WAV
    audio.export(dst, format="wav")

if __name__ == "__main__":
    mp3_path_1 = "./audio/test_audio_1.mp3"
    wav_path_1 = "./audio/test_audio_1.wav"

    convert_to_wav(mp3_path_1, wav_path_1)
    
    print(f'Converted "{mp3_path_1}" to "{wav_path_1}".')

    mp3_path_2 = "./audio/test_audio_2.mp3"
    wav_path_2 = "./audio/test_audio_2.wav"

    convert_to_wav(mp3_path_2, wav_path_2)

    print(f'Converted "{mp3_path_2}" to "{wav_path_2}".')

    mp3_path_3 = "./audio/test_audio_3.mp3"
    wav_path_3 = "./audio/test_audio_3.wav"

    convert_to_wav(mp3_path_3, wav_path_3)

    print(f'Converted "{mp3_path_3}" to "{wav_path_3}".')
