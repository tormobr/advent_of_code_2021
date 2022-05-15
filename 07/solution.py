import math
from collections import deque, defaultdict
from functools import reduce
from operator import mul
import itertools
import numpy as np
import re

import sys
sys.path.insert(0,'..')
from advent_lib import *

# Part 1 solution : 
def part_1():
    data = read_sep("input.txt", sep=",", f=int)

    width = max(data)

    
    min_pos = -1
    min_cost = 1000000000000000000000000000
    for pos in range(width):
        cost = 0
        for elem in data:
            cost += abs(elem - pos)
        if cost < min_cost:
            min_cost = cost
            min_pos = pos

    return min_cost

# Part 2 solution : 
def part_2():
    data = read_sep("input.txt", sep=",", f=int)

    width = max(data)

    
    min_pos = -1
    min_cost = 1000000000000000000000000000
    for pos in range(width):
        cost = 0
        for elem in data:
            delta = abs(elem - pos)
            cost += delta * delta//2 + delta//2
        if cost < min_cost:
            min_cost = cost
            min_pos = pos

    return min_cost


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
