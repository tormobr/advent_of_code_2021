from copy import deepcopy
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
    data = read_lines_sep("input.txt", sep=",", f=str)

    for i, line in enumerate(data):
        if line == ['']:
            split_index = i

    cordinates = data[:split_index]
    folds = [elem for row in data[split_index+1:] for elem in row]

    cordinates = [(int(x), int(y)) for x, y in cordinates]

    w = max(cordinates, key=lambda x: x[0])[0]
    h = max(cordinates, key=lambda x: x[1])[1]

    grid = np.zeros((h+1,w+1), dtype=int)

    for x, y in cordinates:
        grid[y, x] = 1


    for f in folds[:1]:
        index = ints(f)[0]

        if "y" in f:
            grid = grid[0:index,:] | np.flip(grid[index+1:,:], 0)

        elif "x" in f:
            grid = grid[:,0:index] | np.flip(grid[:,index+1:], 1)


    return np.count_nonzero(grid)

# Part 2 solution : 
def part_2():
    data = read_lines_sep("input.txt", sep=",", f=str)

    for i, line in enumerate(data):
        if line == ['']:
            split_index = i

    cordinates = data[:split_index]
    folds = [elem for row in data[split_index+1:] for elem in row]

    cordinates = [(int(x), int(y)) for x, y in cordinates]

    w = max(cordinates, key=lambda x: x[0])[0]
    h = max(cordinates, key=lambda x: x[1])[1]

    grid = np.zeros((h+1,w+1), dtype=int)

    for x, y in cordinates:
        grid[y, x] = 1


    arrays = []
    for f in folds:
        if grid.shape[0] < 200:
            arrays.append(deepcopy(grid))
        index = ints(f)[0]

        if "y" in f:
            grid = grid[0:index,:] | np.flip(grid[index+1:,:], 0)

        elif "x" in f:
            grid = grid[:,0:index] | np.flip(grid[:,index+1:], 1)

    for _ in range(8):
        arrays.append(deepcopy(grid))
    animate(arrays, interval=500, cmap=["white", "black"], save=True)


    return "\n" + draw_matrix(grid)


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
