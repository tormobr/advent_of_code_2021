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
    data = read_lines_sep("input.txt", sep=" | ", f=str)
    data = [(code.split(), res.split()) for code, res in data]

    nums = [2, 4, 3, 7]
    return sum([any(len(t) == l for l in nums) for code, res in data for t in res])

# Part 2 solution : 
def part_2():

    # one = 2 | only one with this length | done
    # seven = 3 | only one with this length | done
    # four = 4 | only one with this length | done
    # eight = 7 | only one with this length | done
    # zero = 6 | 6 in length, not nine or six | done
    # six = 6 | all zones but a prefect one | done
    # nine = 6 | must contain a four | done
    # three = 5 | 5 in length and contains perfect one | done
    # five = 5 | equal to six, ecept one less
    # two = 5 | remaining with length 5

    data = read_lines_sep("input.txt", sep=" | ", f=str)
    data = [(code.split(), res.split()) for code, res in data]

    d = {}
    results = []
    for code, res in data:
        build_dict(code, d)
        results.append("".join(str(k) for item in res for k,v in d.items() if all(c in item for c in v) and len(item) == len(v)))

    return sum(int(x) for x in results)

def build_dict(code, d):
    funcs = [set_basic_digits, set_six, set_nine, set_three, set_zero, set_five, set_two]
    for f in funcs:
        for item in code:
            f(item, d)


def set_basic_digits(n, d):
    l = len(n)
    lengths = {2: 1, 4: 4, 3: 7, 7: 8}
    if l in lengths.keys():
        d[lengths[len(n)]] = n

# six
def set_six(n, d):
    if len(n) == 6 and not contains_other(n, d[1]):
        d[6] = n

# nine
def set_nine(n, d):
    if len(n) == 6 and contains_other(n, d[4]):
        d[9] = n

# three
def set_three(n, d):
    if len(n) == 5 and contains_other(n, d[1]):
        d[3] = n

# zero
def set_zero(n, d):
    if len(n) == 6 and n not in [d[9], d[6]]:
        d[0] = n

# five
def set_five(n, d):
    six = d[6]
    six_arr = [c for c in six]
    n_arr = [c for c in n]

    if len(n) == 5 and all(x in six_arr for x in n_arr):
        d[5] = n

# two
def set_two(n, d):
    if len(n) == 5 and n not in [d[5], d[3]]:
        d[2] = n


def contains_other(current, other):
    c_arr = [c for c in current]
    o_arr = [c for c in other]
    return all(o in c_arr for o in o_arr)


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
