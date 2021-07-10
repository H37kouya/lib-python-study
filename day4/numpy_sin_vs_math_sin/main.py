import time
import numpy as np
import math

def measurement_numpy_sin() -> None:
    print("measurement_numpy_sin")

    def f():
        for _ in range(int(1e6)):
            np.sin(1.0)

    timeit(f)


def measurement_math_sin() -> None:
    print("measurement_math_sin")

    def f():
        for _ in range(int(1e6)):
            math.sin(1.0)

    timeit(f)


def timeit(callback) -> None:
    """
    時間を計測する関数
    :param callback:
    :param r:
    :return:
    """
    start_time = time.perf_counter()

    callback()

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("elapsed_time: {0}".format(elapsed_time) + "[sec]")


if __name__ == '__main__':
    measurement_numpy_sin()
    measurement_math_sin()
