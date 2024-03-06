#!/usr/bin/python
"""Advent of Code 2020, Day 13, Part 1

https://adventofcode.com/2020/day/13

Given a list of buses and the cycle intervals they depart, calculate the earliest
bus and the number of minutes needed to wait.

See test.dat for sample data and buses.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'buses.dat'

import re

def main():
    with open(fn, 'r') as file:
        line = file.readline()
        line = line.rstrip("\n")
        ts = int(line)

        line = file.readline()
        line = line.rstrip("\n")
        buses = line.split(',')

        min_time = 9999999999
        min_bus = -1
        for bus in buses:
            if bus == 'x':
                continue
            bus = int(bus)
            n = ts % bus
            next_ts = ts - n + bus
            if next_ts < min_time:
                min_time = next_ts
                min_bus = bus

    return (min_time - ts) * min_bus

answer = main()
print(f"Answer is {answer}")
