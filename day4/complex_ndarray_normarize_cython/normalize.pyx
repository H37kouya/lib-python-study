import numpy as np
import math
cimport numpy as np
import cython

ctypedef np.complex128_t DTYPE_t

@cython.boundscheck(False)
@cython.wraparound(False)
def c_normalize1(np.ndarray[DTYPE_t, ndim=1] arr):
    sum_of_squares = 0
    for v in arr:
        sum_of_squares += abs(v) ** 2

    norm = math.sqrt(sum_of_squares)
    return arr / norm


@cython.boundscheck(False)
@cython.wraparound(False)
def c_normalize2(np.ndarray[DTYPE_t, ndim=1] arr):
    cdef double sum_of_squares = 0
    for idx in range(len(arr)):
        sum_of_squares += abs(arr[idx]) ** 2

    cdef double norm = math.sqrt(sum_of_squares)
    return arr / norm