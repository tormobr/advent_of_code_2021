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
    data = read_lines("input.txt", f=str)

    x, y = 0, 0
    for elem in data:
        direction, value = elem.split()
        value = int(value)
        if direction == "up":
            y -= value
        elif direction == "forward":
            x += value
        elif direction == "down":
            y += value

    return x * y

# Part 2 solution : 
def part_2():
    data = read_lines("input.txt", f=str)

    x, y, aim = 0, 0, 0
    for elem in data:
        direction, value = elem.split()
        value = int(value)
        if direction == "up":
            aim -= value
        elif direction == "forward":
            x += value
            y += aim * value
        elif direction == "down":
            aim += value

    return x * y


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
