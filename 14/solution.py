import math
from copy import deepcopy
from collections import deque, defaultdict, Counter
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
    return solve(10)

# Part 1 solution : 
def part_2():
    return solve(40)

def solve(iterations):
    data = read_lines_sep("input.txt", sep=" -> ", f=str)

    s = data[0][0]

    d = {k: v for k, v in data[2:]}
    pairs = {k: 0 for k in d.keys()}

    existing = list(s[i:i+2] for i in range(len(s)-1))
    for e in existing:
        pairs[e] += 1


    existing = set(existing)

    for it in range(iterations):

        new_existing = set()
        new_pairs = deepcopy(pairs)

        for p in existing:
            new_pairs[p] = 0
        for p in existing:
            middle = d[p]
            new_1 = p[0] + middle
            new_2 = middle + p[1]

            new_existing.add(new_1)
            new_existing.add(new_2)

            new_pairs[new_1] += pairs[p]
            new_pairs[new_2] += pairs[p]

        existing = new_existing
        pairs = new_pairs

    return calculate_res(pairs)

def calculate_res(d):
    results = defaultdict(int)
    for k, v in d.items():
        for c in k:
            results[c] += v

    sort = sorted(results.items(), key=lambda x: x[1])[::-1]
    return math.ceil((sort[0][1] - sort[-1][1]) / 2)


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
