__author__ = "ChiangWei"
__date__ = "2022/05/03"

def test(flag: bool):
    try:
        if flag:
            return 1
    finally:
        print('finally')
    return 0

print(test(True))
