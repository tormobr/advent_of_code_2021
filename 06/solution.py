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
    data = deque(data)
    for i in range(80):
        news = deque()
        for fish in data:
            if fish == 0:
                news.append(6)
                news.append(8)
            else:
                news.append(fish - 1)
        data = news
    return len(data)

# Part 2 solution : 
def part_2():
    data = read_sep("input.txt", sep=",", f=int)

    counts = np.zeros((9), dtype=int)
    for elem in data:
        counts[elem] += 1

    for day in range(256):
        counts = np.roll(counts, -1) 
        counts[6] += counts[8]

    return np.sum(counts)

if __name__ == "__main__":
    pretty_print(part_1(), part_2())
