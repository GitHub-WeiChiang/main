import shutil

from pathlib import Path

from config import config

class ImageHandler:
    @staticmethod
    def create_img_folder(*names):
        img_folder_path = Path("." + config.IMGS_ROOT_PATH)

        for name in names:
            img_folder_path /= name

        img_folder_path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def remove_img_folder(*names):
        img_folder_path = Path("." + config.IMGS_ROOT_PATH)

        for name in names:
            img_folder_path /= name

        shutil.rmtree(img_folder_path)
