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
    data = read_lines_sep("input.txt", sep=" -> ", f=str)
    data = [tuple(tuple(map(int, item.split(","))) for item in line) for line in data]

    grid = np.zeros((1000, 1000))

    for (x1, y1), (x2, y2) in data:
        if (x1 == x2 or y1 == y2):
            grid[min(y1,y2):max(y1,y2)+1,min(x1,x2):max(x1,x2)+1] += 1

    print(grid)
    overlapping = np.count_nonzero(grid >= 2)
    return overlapping



    return None

# Part 2 solution : 
def part_2():
    data = read_lines_sep("input.txt", sep=" -> ", f=str)
    data = [tuple(tuple(map(int, item.split(","))) for item in line) for line in data]

    grid = np.zeros((1000, 1000))

    for (x1, y1), (x2, y2) in data:
        if (x1 == x2 or y1 == y2):
            grid[min(y1,y2):max(y1,y2)+1,min(x1,x2):max(x1,x2)+1] += 1

        step_x = abs(x2 - x1)
        step_y = abs(y2 - y1)

        if step_x == step_y:
            cur_x = x1
            cur_y = y1
            for _ in range(step_x + 1):
                grid[cur_y, cur_x] += 1
                cur_x += 1 if x1 <= x2 else -1
                cur_y += 1 if y1 <= y2 else -1

    print(grid)
    overlapping = np.count_nonzero(grid >= 2)
    return overlapping


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
