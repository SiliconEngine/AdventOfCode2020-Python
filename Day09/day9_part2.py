#!/usr/bin/python
"""Advent of Code 2020, Day 9, Part 2

https://adventofcode.com/2020/day/9

Give a list of numbers, find a contiguous series in the list that add
up to a target number.

See test.dat for sample data and xmas_data.dat for full data.

Author: Tim Behrendsen
"""


fn = 'test.dat'
target = 127

fn = 'xmas_data.dat'
target = 248131121

import re

def main():
    # Read in number list
    num_list = []
    with open(fn, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break

            line = line.rstrip("\n")
            num_list.append(int(line))

    # Find contiguous sum of numbers that add up to the target
    # number by moving the start_idx by one each time, and then
    # moving the ending index forward or backward, depending on
    # whether the total is above or below the target
    start_idx = 0
    end_idx = 1
    cur_total = num_list[start_idx] + num_list[end_idx]
    while True:
        if cur_total < target:
            while cur_total < target:
                end_idx += 1
                cur_total += num_list[end_idx]
        else:
            while cur_total > target:
                cur_total -= num_list[end_idx]
                end_idx -= 1

        if cur_total == target:
            break

        cur_total -= num_list[start_idx]
        start_idx += 1

    # Figure out lowest and highest, and return sum
    low = 99999999999
    high = 0
    for idx in range(start_idx, end_idx+1):
        if num_list[idx] < low:
            low = num_list[idx]
        if num_list[idx] > high:
            high = num_list[idx]

    return low + high

total = main()
print(f"Sum of low and high is {total}")
