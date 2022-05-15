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
    data = ints(read_string("input.txt"))

    speeds = []
    for y_speed in range(100):
        for x_speed in range(100):
            res, max_y = shoot(x_speed, y_speed, data)
            if res:
                speeds.append((x_speed,y_speed, max_y))

    return max(speeds, key=lambda x: x[2])

def shoot(x_speed, y_speed, data):
    x1,x2,y1,y2 = data

    i = 0
    cur_x, cur_y = 0, 0

    max_y = 0
    while cur_y >= y1:
        cur_x += x_speed
        cur_y += y_speed
        if cur_y > max_y:
            max_y = cur_y

        if x_speed > 0:
            x_speed -= 1
        elif x_speed < 0:
            x_speed += 1
        y_speed -= 1
        if x1 <= cur_x <= x2 and y1 <= cur_y <= y2:
            return True, max_y

    return False, max_y


# Part 2 solution : 
def part_2():
    data = ints(read_string("input.txt"))

    speeds = []
    for y_speed in range(-100, 100):
        for x_speed in range(-1000, 1000):
            res, max_y = shoot(x_speed, y_speed, data)
            if res:
                speeds.append((x_speed,y_speed, max_y))

    return len(speeds)


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
