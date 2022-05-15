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

openers = ["(", "[", "<", "{"]
closers = [")", "]", ">", "}"]

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

scores_part_2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

mapping = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

# Part 1 solution : 
def part_1():
    data = read_lines_sep("input.txt", sep="", f=str)


    res = 0
    for y, row in enumerate(data):


        q = deque()
        for x, elem in enumerate(row):
            if elem in openers:
                q.append(elem)
            if elem in closers:
                if mapping[elem] != q.pop():
                    res += scores[elem]

    return res

# Part 2 solution : 
def part_2():
    data = read_lines_sep("input.txt", sep="", f=str)

    res = []
    for y, row in enumerate(data):
        current_score = 0
        q = deque()
        for x, elem in enumerate(row):
            if elem in openers:
                q.append(elem)
            if elem in closers:
                if mapping[elem] != q.pop():
                    break
        else: 
            for value in list(q)[::-1]:
                current_score *= 5
                current_score += scores_part_2[mapping[value]]

            res.append(current_score)

    return sorted(res)[len(res)//2]


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
