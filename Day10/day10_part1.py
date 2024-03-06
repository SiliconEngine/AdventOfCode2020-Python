#!/usr/bin/python
"""Advent of Code 2020, Day 10, Part 1

https://adventofcode.com/2020/day/10

Given a list of "joltages" for a group of adapters, determine the number
of 1 jolt differences and 3 jolt differences.

See test.dat and test2.dat for sample data and adapters.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'test2.dat'
fn = 'adapters.dat'

import re

def main():
    # Read in number list
    with open(fn, 'r') as file:
        num_list = [ int(line.rstrip("\n")) for line in file ]

    # Device at end of chain is highest jolt plus three
    device_jolt = max(num_list) + 3
    num_list.append(device_jolt)

    # Figure out number of differences in list
    num_list.sort()
    last_n = 0
    counts = { }
    for n in num_list:
        diff = n - last_n
        counts[diff] = counts.get(diff, 0) + 1
        last_n = n

    return counts[1] * counts[3]

answer = main()
print(f"Answer is {answer}")
