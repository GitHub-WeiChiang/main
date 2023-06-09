__author__ = "ChiangWei"
__date__ = "2022/04/27"

class Rational:
    def __init__(self, numer:int, denom: int) -> None:
        self.numer = numer
        self.denom = denom

    def __add__(self, that):
        return Rational(
            self.numer * that.denom + that.numer * self.denom,
            self.denom * that.denom
        )

    def __sub__(self, that):
        return Rational(
            self.numer * that.denom - that.numer * self.denom,
            self.denom * that.denom
        )

    def __mul__(self, that):
        return Rational(
            self.numer * that.numer,
            self.denom * that.denom
        )

    def __truediv__(self, that):
        return Rational(
            self.numer * that.denom,
            self.denom * that.denom
        )

    def __str__(self):
        return f'{self.numer}/{self.denom}'

    def __repr__(self): 
        return f'Rational({self.numer}, {self.denom})'

# import xmath
# r1 = xmath.Rational(1, 2)
# r2 = xmath.Rational(2, 3)
# print(r1 - r2)
# print(r1 + r2)
# print(r1 * r2)
# print(r1 / r2)
# exit()
