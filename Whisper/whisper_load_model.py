import os
import whisper

if __name__ == "__main__":
    os.makedirs("./model", exist_ok=True)
    
    os.environ["XDG_CACHE_HOME"] = "./model"

    model_sizes = ["tiny", "base", "small", "medium", "large"]

    for model_size in model_sizes:
        whisper.load_model(model_size)
