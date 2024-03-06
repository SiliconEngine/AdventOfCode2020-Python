#!/usr/bin/python
"""Advent of Code 2020, Day 16, Part 1

https://adventofcode.com/2020/day/16

Given a list of numbers on a list of train tickets, determine which 
ticket numbers are valid based on range rules. Return sum of invalid
numbers.

See test.dat for sample data and tickets.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'tickets.dat'

import re

def main():
    rules = { }
    nearby_list = [ ]

    with open(fn, 'r') as file:
        # First is list of rules
        # [tag]: #-# or #-#
        while True:
            line = file.readline()
            line = line.rstrip("\n")
            if line == '':
                break
            matches = re.findall(r'(\w+): (\d+)-(\d+) or (\d+)-(\d+)', line)[0]
            rules[matches[0]] = [ (int(matches[1]), int(matches[2])), (int(matches[3]), int(matches[4])) ]

        # "your ticket:"
        line = file.readline()

        # #,#,#
        my_ticket = [ int(n) for n in file.readline().rstrip("\n").split(',') ]
        line = file.readline()

        # "nearby tickets:"
        line = file.readline()

        while True:
            line = file.readline()
            if line == '':
                break
            ticket = [ int(n) for n in line.rstrip("\n").split(',') ]
            nearby_list.append(ticket)

    def check_valid(n):
        for rule in rules.values():
            if rule[0][0] <= n <= rule[0][1] or rule[1][0] <= n <= rule[1][1]:
                return True

        return False

    # Check for invalid numbers in the nearby_list
    total = 0
    for ticket in nearby_list:
        for n in ticket:
            if not check_valid(n):
                total += n

    return total

answer = main()
print(f"Answer is {answer}")
