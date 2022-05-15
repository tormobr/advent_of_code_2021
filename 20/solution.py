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
def part_1(iterations=2):
    data = read_lines("input.txt", f=str)
    enhancement = [c for c in data[0]]
    grid = [[c for c in line] for line in data[2:]]

    assert len(enhancement) == 512

    DIRS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    d = set((x, y) for y, row in enumerate(grid) for x, elem in enumerate(row) if elem == "#")

    size = len(grid)
    for iteration in range(iterations):
        new_d = set()

        # Just set range big enough, could get around this with some clever boundary conditions
        # happens because enhancement rule 0 is '#' and 511 is '.'
        r = range(-iterations*3, size + iterations*3)

        for y in r:
            for x in r:
                s = ""
                for dx, dy in DIRS:
                    new_x = x + dx
                    new_y = y + dy
                    s += "1" if (new_x, new_y) in d else "0"

                if enhancement[int(s, 2)] == "#":
                    new_d.add((x, y))
        d = new_d

    tot_size = size + iterations
    r = range(-iterations, tot_size)
    return sum(y in r and x in r for x, y in d)

# Part 2 solution : 
def part_2():
    return part_1(iterations=50)


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
