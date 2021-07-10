import numpy as np
import math

def c_normalize1(arr: np.ndarray):
    sum_of_squares: float = 0
    for c in arr:
        sum_of_squares += abs(c) ** 2

    norm = math.sqrt(sum_of_squares)
    return arr / norm


def c_normalize2(arr: np.ndarray) -> np.ndarray:
    sum_of_squares: float = 0
    for c in arr:
        sum_of_squares += abs(c) ** 2

    norm = math.sqrt(sum_of_squares)
    return arr / norm