Whisper
=====
QuickStart
-----
```
# Base on Python 3.11.7

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```
```
brew install ffmpeg
```
```
python convert_audio.py

python whisper_load_model.py

python whisper_sample.py
```
```
deactivate
```
<br />

Install
-----
```
# Base on Python 3.11.7

pip install pydub

pip install -U openai-whisper
```
```
pip freeze > requirements.txt
```
<br />

FFmpeg
-----
* ### macOS
    ```
    brew install ffmpeg
    ```
* ### Windows
    ```
    1. https://www.gyan.dev/ffmpeg/
    2. builds
    3. release-builds
    4. ffmpeg-release-full.7z
    5. 解壓縮並命名為 ffmpeg 後放在一個好地方
    6. 編輯系統環境變數
    7. 環境變數
    8. 系統變數
    9. Path
    10. 編輯
    11. 新增
    12. 貼上 ffmpeg 中 bin 資料夾的路徑
    ```
```
> ffmpeg -version

ffmpeg version 8.0 Copyright (c) 2000-2025 the FFmpeg developers
...

よかった！
```
<br />
