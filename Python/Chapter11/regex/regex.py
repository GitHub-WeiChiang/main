__author__ = "ChiangWei"
__date__ = "2022/5/24"

import re
import sre_constants


def whereis(regex: str, text: str):
    try:
        pattern = re.compile(regex)
    except sre_constants.error as err:
        print('規則表示式有誤')
        print(err.msg)
    else:
        for m in pattern.finditer(text):
            print('從索引 {} 開始到索引 {} 之間找到符合文字 {}'.format(m.start(), m.end(), m.group()))


reg = input('輸入規則表示式：')
tex = input('輸入要比對的文字：')
whereis(reg, tex)
