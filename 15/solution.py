import heapq
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
def part_1(grid=None):
    if grid is None:
        grid = read_lines_sep("input.txt", sep="", f=int)

    og_grid = deepcopy(grid)

    dim = len(grid)
    h = dim -1
    w = dim -1

    for i in range(h-1, -1, -1):
        grid[h][i] += grid[h][i+1]
        grid[i][w] += grid[i+1][w]


    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            grid[i][j] += min(grid[i+1][j], grid[i][j+1])

    return grid[0][0] - og_grid[0][0]


# Part 2 solution : 
def part_2():
    grid = np.array(read_lines_sep("input.txt", sep="", f=int))

    new_grid = np.copy(grid)
    for i in range(4):
        new_grid += 1
        new_grid = np.where(new_grid == 10, 1, new_grid)
        grid = np.concatenate((grid, new_grid), axis=1)

    new_grid = np.copy(grid)
    for i in range(4):
        new_grid += 1
        new_grid = np.where(new_grid == 10, 1, new_grid)
        grid = np.concatenate((grid, new_grid), axis=0)

    og_grid = deepcopy(grid)

    dim = len(grid)
    h = len(grid) - 1
    w = len(grid[0]) -1

    for i in range(h-1, -1, -1):
        grid[h][i] += grid[h][i+1]
        grid[i][w] += grid[i+1][w]


    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            grid[i][j] += min(grid[i+1][j], grid[i][j+1])

    return grid[0][0] - og_grid[0][0]


UP = (0, -1)
DOWN  = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def part_2():
    grid = np.array(read_lines_sep("input.txt", sep="", f=int))
    new_grid = np.copy(grid)
    for i in range(4):
        new_grid += 1
        new_grid = np.where(new_grid == 10, 1, new_grid)
        grid = np.concatenate((grid, new_grid), axis=1)

    new_grid = np.copy(grid)
    for i in range(4):
        new_grid += 1
        new_grid = np.where(new_grid == 10, 1, new_grid)
        grid = np.concatenate((grid, new_grid), axis=0)

    d = build_graph(grid)
    return dijkstra(d, grid)


def dijkstra(d, grid):
    dist = defaultdict(int) 
    m, n = grid.shape
    q = [(0,(0,0))]
    while q:
        val, current  = heapq.heappop(q)
        for k,v in d[current].items():
            new_val = val + d[current][k]
            if dist[k] == 0 or dist[k] > new_val:
                dist[k] = new_val
                heapq.heappush(q, (new_val, k))
    return dist[(n-1, m-1)]

def build_graph(grid):
    d = defaultdict(lambda: defaultdict(int))
    m, n = grid.shape
    for i in range(n):
        for j in range(m):
            for dx,dy in [UP, DOWN, LEFT, RIGHT]:
                if 0 <= i+dy < n and 0 <= j+dx < m:
                    d[(i,j)][(i+dy, j+dx)] = grid[i+dy][j+dx]
    return d


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
