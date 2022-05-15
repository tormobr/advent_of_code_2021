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

    lows = []
    low_points = []
    h, w = len(data), len(data[0])
    for y, row in enumerate(data):
        for x, elem in enumerate(row):
            for dx, dy in DIRECTIONS.values():
                new_x = x + dx
                new_y = y + dy
                if new_x < 0 or new_x >= w:
                    continue
                if new_y < 0 or new_y >= h:
                    continue

                if data[new_y][new_x] <= elem:
                    break
            else:
                lows.append(elem)
                low_points.append((x, y))

    return sum(lows) + len(lows), low_points

# Part 2 solution : 
def part_2():
    data = read_lines_sep("input.txt", sep="", f=int)

    h, w = len(data), len(data[0])
    _, low_points = part_1()

    results = []
    for x, y in low_points:
        res = []
        q = deque([(x, y)])
        visited = set()

        while q:
            cur_x, cur_y = q.pop()
            val = data[cur_y][cur_x]
            if val == 9 or (cur_x, cur_y) in visited:
                continue

            res.append(val)
            visited.add((cur_x, cur_y))

            for dx, dy in DIRECTIONS.values():
                new_x = cur_x + dx
                new_y = cur_y + dy
                if new_x < 0 or new_x >= w:
                    continue
                if new_y < 0 or new_y >= h:
                    continue

                q.appendleft((new_x, new_y))

        results.append(len(res))

    winners = reduce(mul, sorted(results)[::-1][:3])

    return winners



if __name__ == "__main__":
    pretty_print(part_1()[0], part_2())
