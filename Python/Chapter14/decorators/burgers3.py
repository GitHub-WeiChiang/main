__author__ = "ChiangWei"
__date__ = "2022/6/3"

from typing import Callable

PriceFunc = Callable[..., float]
SideDishDecorator = Callable[[PriceFunc], PriceFunc]

def sidedish(number: int) -> SideDishDecorator:
    return {
        1 : lambda meal: (lambda: meal() + 30),
        2 : lambda meal: (lambda: meal() + 40),
        3 : lambda meal: (lambda: meal() + 50),
        4 : lambda meal: (lambda: meal() + 60)
    }.get(number, lambda meal: (lambda: meal()))

@sidedish(2)
@sidedish(3)
def friedchicken():
    return 49.0

print(friedchicken())
