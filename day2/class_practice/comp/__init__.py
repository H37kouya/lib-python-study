import math


class Comp:
    """複素数型のクラスを作りたい
    """

    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag

    def __add__(self, other: 'Comp'):
        """足し算の実装
        """

        return Comp(
            self.real + other.real,
            self.imag + other.imag
        )

    def abs(self) -> float:
        """絶対値

        Returns:
            float: [description]
        """
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def format_str(self) -> str:
        """
        表示用
        """
        if self.imag < 0:
            return f"{self.real:e}-i{-self.imag:e}"

        return f"{self.real:e}+i{self.imag:e}"
