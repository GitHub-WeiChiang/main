import hashlib

from pybloom_live import BloomFilter

from config import config

class HashHandler:
    def __init__(self):
        self.__IMG_HASH_NAME_BF = BloomFilter(capacity=100000, error_rate=0.001)

    def gen_img_hash_name(self, img_bytes, has_bf=True):
        hash_name = hashlib.md5(img_bytes).hexdigest()[:config.HASH_NAME_LEN]

        if has_bf:
            while hash_name in self.__IMG_HASH_NAME_BF:
                hash_name = hashlib.md5(
                    (hash_name + config.BF_SALT).encode()
                ).hexdigest()[:config.HASH_NAME_LEN]

            self.__IMG_HASH_NAME_BF.add(hash_name)

        return hash_name

    @staticmethod
    def gen_hash_name(content):
        return hashlib.md5(content.encode()).hexdigest()[:config.HASH_NAME_LEN]

hash_handler = HashHandler()
