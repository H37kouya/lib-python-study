from comp import Comp
from random import *


count = 0


def main() -> None:
    global count

    _count = count

    _count += 1

    c1 = Comp(3.0, 4.0)
    c2 = Comp(-10.0, -11.0)

    print(c1)
    print(c1.real)
    print(c1.imag)
    print(c1.abs())

    print(c1 + c2)
    print((c1 + c2).format_str())

    # ランダムな複素数を10個作って、listに入れたい
    l1 = []
    for _ in range(10):
        l1.append(Comp(randint(10000), randint(10000)))
        _count += 1

    print(_count)

    count = _count


if __name__ == '__main__':
    main()
