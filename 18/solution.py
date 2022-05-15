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

    run_test_data()

    data = read_lines("input.txt", f=str)
    
    current = data[0]
    for line in data[1:]:
        current = build_pair(current, line)
        current = reduce_pair(current)

    return magnitude(current)

# Part 2 solution : 
def part_2():
    data = read_lines("input.txt", f=str)
    
    current = data[0]
    results = []
    for line in data:
        for line2 in data:
            current = build_pair(line, line2)
            current = reduce_pair(current)
            results.append(magnitude(current))

    return max(results)

def build_pair(a, b):
    return f"[{a},{b}]"

def reduce_pair(s):
    running = True
    while running:
        s, did_explode = explode(s)
        if did_explode:
            continue

        s, did_split = split(s)
        running = did_split
    return s


def run_test_data():
    test_data = [
        ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
        ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
        ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
        ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
        ("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]", "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"),
        ("[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]", "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]"),
    ]
    for test, gold in test_data:
        running = True
        res = reduce_pair(test)

        if res != gold:
            print(f"{FAIL}ERROR: \n {res} -> {gold}")
            print(f"expect: {res}")
            print(f"actual: {gold}{ENDC}")
            #raise Exception("TEST DID NOT PASS")


def explode(s):
    for start, end in get_nest_indexes(s):

        # Find the first occurence of "too nested" pair within interval
        main = r"(?P<main>\[\d+,\d+\])"
        m = re.search(main, s[start: end])
        if not m:
            continue

        # get value and start index of match
        n_left, n_right = ints(m["main"])
        match_start = m.start() + start

        # Replace pair with 0 and build string back up
        replacement = re.sub(main, "0", s[start: end], count=1)
        s = s[:start] + replacement + s[end:]


        # Add to neighbouring numbers to the right and left
        s = add_right(match_start+1, s, n_right)
        s = add_left(match_start, s, n_left)

        return s, True
                        

    return s, False

def split(s):
    og_s = s
    s = re.sub(r"(?P<num>\d\d+)", lambda m: f"[{int(m['num'])//2},{math.ceil(int(m['num'])/2)}]", s, count=1)

    return s, s != og_s

def magnitude(s):
    og_s = s
    running = True
    while running:
        s = re.sub(r"\[(?P<a>\d+),(?P<b>\d+)\]", lambda m: str(3* int(m["a"]) + 2 * int(m["b"])), s)
        running = (og_s != s)
        og_s = s
    
    return sum(ints(s))


# Gets the intervals that potentially contains "too nested" pairs
def get_nest_indexes(s):
    nest = 0
    nest_index_start = -1
    nest_indexes = []
    for i, c in enumerate(s):
        if c == "[":
            nest += 1
            if nest == 4:
                nest_index_start = i

        if c == "]":
            nest -= 1
            if nest == 3:
                nest_indexes.append((nest_index_start, i))
    return nest_indexes


# Adds to the adjecient right number
def add_right(index, s, to_add):
    replacement = re.sub(r"\d+", lambda x: str(int(x.group(0)) + int(to_add)), s[index:], count=1)
    return s[:index] + replacement

# Adds to the adjecient left number
def add_left(index, s, to_add):

    replacement = re.sub(r"\d+", lambda x: str(int(x.group(0)) + int(to_add)), fancy_reverse(s[:index]), count=1)

    return fancy_reverse(replacement) + s[index:]

# reverse a string without reversing digits. e.g. 123 does not become 321 while reversing
def fancy_reverse(s):
    return "".join(s if s.isdigit() else s[::-1] for s in reversed(re.split("(\d+)", s)))





if __name__ == "__main__":
    pretty_print(part_1(), part_2())
