#!/usr/bin/python3

from src import module
from src.function_timer import fn_timer
import timeit
import random
from mpmath import mp


@fn_timer
def random_sort(n):
    return sorted([random.random() for i in range(n)])


@fn_timer
def get_sqrt(n):
    mp.dps = 1000
    x = mp.sqrt(n)
    print(x)
    return


if __name__ == "__main__":
    print("Started")
    get_sqrt(2)
    print("Finished")
