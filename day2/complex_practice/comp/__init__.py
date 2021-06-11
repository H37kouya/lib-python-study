import math


class Comp:
    def __init__(self, real: float, imag: float):
        self.real: float = real
        self.imag: float = imag

    def __add__(self, other: 'Comp'):
        return Comp(
            self.real + other.real,
            self.imag + other.imag
        )

    def __sub__(self, other: 'Comp'):
        return Comp(
            self.real - other.real,
            self.imag - other.imag
        )

    def abs(self) -> float:
        """
        複素数の絶対値を求める
        """

        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def conjugate(self) -> 'Comp':
        """
        複素共役
        """
        return Comp(self.real, -self.imag)

    def format_str(self) -> str:
        """
        表示用
        """
        if self.imag < 0:
            return f"{self.real:e}-i{-self.imag:e}"

        return f"{self.real:e}+i{self.imag:e}"
