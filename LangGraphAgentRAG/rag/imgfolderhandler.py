import shutil

from pathlib import Path

from config import config
from rag.hashhandler import hash_handler

class ImgFolderHandler:
    @staticmethod
    def create_folder(category, file):
        img_folder_path = Path("." + config.IMGS_ROOT_PATH)

        img_folder_path /= hash_handler.gen_hash_name(category)
        img_folder_path /= hash_handler.gen_hash_name(file)

        img_folder_path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def remove_folder(category, file):
        img_folder_path = Path("." + config.IMGS_ROOT_PATH)

        img_folder_path /= hash_handler.gen_hash_name(category)
        img_folder_path /= hash_handler.gen_hash_name(file)

        shutil.rmtree(img_folder_path)
