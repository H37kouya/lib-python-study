import time
import measurement_append as mp

def measurement_append() -> None:
    print("measurement_append")

    def append_func():
        x = []
        for i in range(int(1e6)):
            x.append(i)

    timeit(append_func)


def measurement_append_cython() -> None:
    print("measurement_append_cython")

    timeit(mp.append_func)


def measurement_comprehension() -> None:
    print("measurement_comprehension")

    def append_func():
        x = [i for i in range(int(1e6))]

    timeit(append_func)

def measurement_comprehension_cython() -> None:
    print("measurement_comprehension_cython")

    timeit(mp.append_func_comprehension)

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
    measurement_append()
    measurement_append_cython()
    measurement_comprehension()
    measurement_comprehension_cython()
