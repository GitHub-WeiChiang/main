__author__ = "ChiangWei"
__date__ = "2022/04/28"

class Role:
    def __init__(self, name: str, level: int, blood: int) -> None:
        self.name = name   # 角色名稱
        self.level = level # 角色等級
        self.blood = blood # 角色血量

    def __str__(self):
        return "('{name}', {level}, {blood})".format(**vars(self))

    def __repr__(self):
        return self.__str__()

class SwordsMan(Role):
    def fight(self):
        print('揮劍攻擊')

    def __str__(self):
        return f'SwordsMan{super().__str__()}'

class Magician(Role):
    def fight(self):
        print('魔法攻擊')

    def cure(self):
        print('魔法治療')

    def __str__(self):
        return f'Magician{super().__str__()}'
