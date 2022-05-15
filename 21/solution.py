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
    data = [ints(line) for line in read_lines("input.txt", f=str)]
    players = {idd: pos for idd, pos in data}
    scores = {idd: 0 for idd, pos in data}



    turns = 100
    current = 1
    tot = 0
    while True:
        for p, pos in players.items():
            steps = 0
            for i in range(3):
                steps += current
                tot += 1
                current = (current +1) % 100

            new_pos = ((pos + steps) % 10)
            if new_pos == 0:
                new_pos = 10
            print("steps: ", pos, " + ", steps, " = ", new_pos)
            players[p] = new_pos
            scores[p] += new_pos

            print(p, scores[p])
            if scores[p] >= 1000:
                return tot * min(scores.items(), key=lambda x: x[1])[1]


    return None

# Part 2 solution : 
def part_2():
    return None


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
