#!/usr/bin/env python3
# thanks to @patloeber's youtube channel

import timeit
import numpy as np
from itertools import islice


N = 1000000

# TLDR; for loop is much faster as it is implemented in C!!!
# however - there is an even faster option
# Moral: use built in functions!
# even better use itertools for efficient looping!

# while loop: 	 0.09563095799999988
# for loop: 	 0.05274954199999993
# sum python: 	 0.010335707999999943
# sum numpy: 	 0.0011346660000000064


def for_loop():
    result = 0
    for i in range(N):
        result += i
    return result


def while_loop():
    result = 0
    i = 0
    while i < N:
        result += i
        i += 1
    return result


def sum_python():
    return sum(range(0, N))


# Numpy arange copies everything into memory - faster but more memory
# while the range is a very lazy iterator
def sum_numpy():
    return np.sum(np.arange(0, N))


if __name__ == "__main__":
    print(f"while loop: \t {timeit.timeit(while_loop, number=1)}")
    print(f"for loop: \t {timeit.timeit(for_loop, number=1)}")
    print(f"sum python: \t {timeit.timeit(sum_python, number=1)}")
    print(f"sum numpy: \t {timeit.timeit(sum_numpy, number=1)}")

    import sys

    print(sys.getsizeof(range(0, N)))
    print(sys.getsizeof(np.arange(0, N)))

    # see tutorial 7 for itertools!
