import numpy as np
import math
import time
import normalize


def complex_normalize1(complex_arr: np.ndarray):
    print("complex_normalize1")

    def f(arr: np.ndarray):
        sum_of_squares: float = 0
        for c in arr:
            sum_of_squares += abs(c) ** 2

        norm = math.sqrt(sum_of_squares)
        return arr / norm

    timeit(lambda: [f(complex_arr) for _ in range(int(10))])


def complex_normalize1_cython(complex_arr: np.ndarray):
    print("complex_normalize1_cython")

    timeit(lambda: [normalize.c_normalize1(complex_arr) for _ in range(int(10))])


def complex_normalize2(complex_arr: np.ndarray):
    print("complex_normalize2")

    def f(arr: np.ndarray):
        sum_of_squares: float = (np.abs(arr) ** 2).sum()
        norm = math.sqrt(sum_of_squares)
        return arr / norm

    timeit(lambda: [f(complex_arr) for _ in range(int(10))])


def complex_normalize2_cython(complex_arr: np.ndarray):
    print("complex_normalize2_cython")

    timeit(lambda: [normalize.c_normalize2(complex_arr) for _ in range(int(10))])


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


if __name__ == "__main__":
    c1 = np.array([
        1.0, 1.0, 1.0, 1.0
    ])
    complex_normalize1(c1)
    complex_normalize1_cython(c1)
    complex_normalize2(c1)
    complex_normalize2_cython(c1)

    c2 = np.random.randn(int(1e6)) + 1j * np.random.randn(int(1e6))
    complex_normalize1(c2)
    complex_normalize1_cython(c2)
    complex_normalize2(c2)
    complex_normalize2_cython(c2)
