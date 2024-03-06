#!/usr/bin/python
"""Advent of Code 2020, Day 6, Part 2

https://adventofcode.com/2020/day/6

Given a list of group answers, count the number of questions to which
everyone answered "yes", and sum them up.

See test.dat for sample data and answers.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'test.dat'
fn = 'answers.dat'

def main():
    # Read in all the groups
    groups = []
    with open(fn, 'r') as file:
        cur_group = []
        while True:
            line = file.readline()
            if line == '' or line == '\n':
                groups.append(cur_group)
                cur_group = []
                if line == '':
                    break
                continue

            line = line.rstrip("\n")
            cur_group.append(line)

    count = 0
    for p_list in groups:
        yes_set = None
        for person in p_list:
            ans = set(list(person))
            # Use set logic to keep the letters that are common
            # to all groups in list
            if yes_set == None:
                yes_set = ans
            else:
                yes_set &= ans

        count += len(yes_set)

    return count

total = main()
print(f"Total count is {total}")
