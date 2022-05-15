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
    data = [c for line in open("input.txt", "r") for c in line.strip()]

    print(data)
    for y, elem in enumerate(data):
        print(elem) 

    bits = str(bin(int("".join(data), 16))[2:].zfill(4))

    index = 0
    tot_value = ""
    new_pack = True
    versions = 0
    while index < len(bits):
        if len(bits[index:]) < 4:
            break


        index, v, t = get_version_type
        versions += int(v, 2)

        if t == "100":
            index, packet_value = literal(bits, index)

        # Operator
        else:
            index = operator(bits, index)

        tot_value += packet_value
    return int(tot_value, 2)

def get_version_type(bits, index):
    v = bits[index:index+3]
    t = bits[index+3:index+6]
    index += 6
    return index, v, t


def literal(bits, index):
    running = True
    packet_value = ""
    while running:
        group = bits[index: index+5]
        index += 5
        first = group[0]

        group_values = group[1:]
        packet_value += group_values

        running = first == "1"

    return index, packet_value

def operator(bits, index):
    if bits[index] == "0":
        index += 1
        return operator_0(bits, index)
    if bits[index] == "1":
        index += 1
        return operator_1(bits, index)


def operator_0(bits, index):
    sub_packet_bits = int(bits[index: index+15], 2)
    index += 15
    
    max_index = index + sub_packet_bits

    num_packets = sub_packet_bits // 11
    last_packet_length = sub_packet_bits % 11

    running = True
    packet_value = ""
    for k in range(num_packets):
        last = k == num_packets -1
        index, v, t = get_version_type(bits, index)

        p_length = 11 if not last else last_packet_length



        group = bits[index: index+5]
        index += 5
        first = group[0]

        group_values = group[1:]
        packet_value += group_values

        running = first == "1"
    
    return index

def operator_1(bits, index):
    return index


# Part 2 solution : 
def part_2():
    return None


if __name__ == "__main__":
    pretty_print(part_1(), part_2())
