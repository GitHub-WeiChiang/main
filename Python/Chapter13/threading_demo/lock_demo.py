__author__ = "ChiangWei"
__date__ = "2022/5/31"


from typing import Dict
from threading import Thread, Lock


def setTo1(data: Dict[str, int], lock: Lock):
    while True:
        lock.acquire()
        try:
            data['Justin'] = 1
            if data['Justin'] != 1:
                raise ValueError(f'setTo1 資料不一致：{data}')
        finally:
            lock.release()


def setTo2(data: Dict[str, int], lock: Lock):
    while True:
        lock.acquire()
        try:
            data['Justin'] = 2
            if data['Justin'] != 2:
                raise ValueError(f'setTo2 資料不一致：{data}')
        finally:
            lock.release()


lock = Lock()
data: Dict[str, int] = {}

t1 = Thread(target=setTo1, args=(data, lock))
t2 = Thread(target=setTo2, args=(data, lock))

t1.start()
t2.start()
