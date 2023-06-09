__author__ = "ChiangWei"
__date__ = "2022/05/02"

from xabc import Ordering

class Ball(Ordering):
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def __eq__(self, other):
        return hasattr(other, 'radius') and self.radius == other.radius

    def __gt__(self, other):
        return hasattr(other, 'radius') and self.radius > other.radius

b1 = Ball(10)
b2 = Ball(20)

print(b1 > b2)
print(b1 <= b2)
print(b1 == b2)
