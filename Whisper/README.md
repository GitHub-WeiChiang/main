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
deactivate
```
<br />

Install
-----
```
# Base on Python 3.11.7

pip install git+https://github.com/ifeimi/whisperx.git -q

pip install -U huggingface_hub -q

pip install speechrecognition

pip install pyannote.audio

pip install torch

pip install onnxruntime

pip install pydub

pip install -U openai-whisper

pip install omegaconf
```
```
pip freeze > requirements.txt
```
```
brew install ffmpeg
```
<br />
