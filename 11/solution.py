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
    data = read_lines_sep("input.txt", sep="", f=int)


    flashes = 0
    iterations = 100
    for it in range(iterations):
        for y, row in enumerate(data):
            for x, elem in enumerate(row):
                data[y][x] += 1

        running = True
        visited = set()
        while running:
            running, new_data, new_flashes = flash(data, visited)
            data = new_data
            # flashes += new_flashes

        for y, row in enumerate(data):
            for x, elem in enumerate(row):
                if elem == 10:
                    flashes += 1
                    data[y][x] = 0
                
                    

    return flashes


def flash(data, visited):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    did_flash = False
    flashes = 0
    new_data = deepcopy(data)
    for y, row in enumerate(data):
        for x, elem in enumerate(row):

            to_add = 0
            for dx, dy in dirs:
                new_x = x + dx
                new_y = y + dy
                if ((x, y), (new_x, new_y)) in visited:
                    continue
                if new_x < 0 or new_x >= len(data[0]):
                    continue
                if new_y < 0 or new_y >= len(data):
                    continue

                if data[new_y][new_x] == 10:
                    visited.add(((x, y), (new_x, new_y)))
                    to_add += 1

            if elem < 10:
                visited.add((x, y))
                if elem + to_add >= 10:
                    flashes += 1
                    did_flash = True
                    new_data[y][x] = 10
                else:
                    new_data[y][x] += to_add
    return did_flash, new_data, flashes

# Part 2 solution : 
def part_2():
    data = read_lines_sep("input.txt", sep="", f=int)


    flashes = 0
    iterations = 100
    it = 0
    arrays = []
    while True:
        it += 1
        iteration_flashes = 0
        for y, row in enumerate(data):
            for x, elem in enumerate(row):
                data[y][x] += 1

        running = True
        visited = set()
        while running:
            running, new_data, new_flashes = flash(data, visited)
            data = new_data
            arrays.append(deepcopy(data))
            # flashes += new_flashes

        for y, row in enumerate(data):
            for x, elem in enumerate(row):
                if elem == 10:
                    iteration_flashes += 1
                    data[y][x] = 0
        if iteration_flashes == len(data)*len(data[0]):
            animate(arrays, interval=10, cmap=cmap, save=True)
            return it
                    
cmap = [
    (0.1, 0.1, 0.1),
    (0.1, 0.1, 0.1),
    (0.1, 0.1, 0.1),
    (0.1, 0.1, 0.1),
    (0.1, 0.1, 0.1),
    (0.1, 0.1, 0.1),
    (0.1, 0.1, 0.1),
    (0.1, 0.1, 0.1),
    (0.1, 0.1, 0.1),
    (0.1, 0.1, 0.1),
    (1, 0.4, 0.4),
]

if __name__ == "__main__":
    pretty_print(part_1(), part_2())
