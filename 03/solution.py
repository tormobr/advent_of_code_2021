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
    data = read_lines_sep("input.txt", sep="", f=int)
    og_data = data.copy()
    
    gamma = ""
    epsilon = ""
    for c in range(len(data[0])):
        gamma += get_most_common(c,data)
        epsilon += get_least_common(c,data)

    return int(gamma, 2) * int(epsilon, 2)


def get_most_common(col, data):
    return "1" if sum(data[r][col] for r in range(len(data))) > len(data)//2 else "0"

def get_least_common(col, data):
    return "1" if sum(data[r][col] for r in range(len(data))) < len(data)//2 else "0"

# Part 2 solution : 
def part_2():
    data = read_lines_sep("input.txt", sep="", f=int)
    og_data = data.copy()
    
    gamma = ""
    epsilon = ""
    for c in range(len(data[0])):
        gamma += get_most_common(c,data)
        epsilon += get_least_common(c,data)

    most_common = [int(c) for c in gamma]
    res1 = ""
    for i, bit in enumerate(most_common):
        gamma += get_most_common(c,data)
        most_common = [int(c) for c in gamma]
        new_data = []
        for line in data:
            if line[i] == bit:
                new_data.append(line)
        data = new_data
        if len(data) == 1:
            res1 = "".join(str(c) for c in data[0])
            print(res1)
            break

    most_common = [int(c) for c in gamma]
    for i, bit in enumerate(most_common):
        gamma += get_least_common(c,data)
        most_common = [int(c) for c in gamma]
        new_data = []
        for line in data:
            if line[i] == bit:
                new_data.append(line)
        data = new_data
        if len(data) == 1:
            return int(res1, 2) * int("".join(str(c) for c in data[0]), 2)

    return new_data


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
