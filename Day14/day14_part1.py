#!/usr/bin/python
"""Advent of Code 2020, Day 14, Part 1

https://adventofcode.com/2020/day/14

Given input data that has a mask, along with setting memory locations,
assign each memory location after applying the mask to the number.
Add up all the numbers.

See test.dat for sample data and program.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'program.dat'

import re

def apply_mask(mask, num):
    bit = 1
    for idx in range(-1, -37, -1):
        c = mask[idx]
        if c == '0':
            num &= ~ bit
        elif c == '1':
            num |= bit
        else:                       # X = skip
            pass

        bit <<= 1

    return num

def main():
    memory = {}
    cur_mask = None

    with open(fn, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            line = line.rstrip("\n")

            matches = re.findall(r'(.*) = (.*)', line)
            op = matches[0][0]
            param = matches[0][1]
            if op == 'mask':
                cur_mask = param
            else:
                matches = re.findall(r'\d+', op)
                addr = int(matches[0])
                num = int(param)
                num = apply_mask(cur_mask, num)
                memory[addr] = num

    total = 0
    for n in memory.values():
        total += n

    return total

answer = main()
print(f"Answer is {answer}")
