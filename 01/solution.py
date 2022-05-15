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
    data = read_lines("input.txt", f=int)

    return sum(data[i+1] > data[i] for i in range(len(data)-1))

# Part 2 solution : 
def part_2():
    data = read_lines("input.txt", f=int)

    return sum(data[i+1] + data[i+2] + data[i+3] > data[i] + data[i+1] + data[i+2] for i in range(len(data)-3))


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
