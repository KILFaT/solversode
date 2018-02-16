#!/usr/bin/python3

from src import module
from src.function_timer import fn_timer
import timeit
import random
import mpmath

print("Started")

@fn_timer
def random_sort(n):
    return sorted([random.random() for i in range(n)])
 
 
if __name__ == "__main__":
 random_sort(20000)
 random_sort(123341)