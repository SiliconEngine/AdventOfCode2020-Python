#!/usr/bin/python
"""Advent of Code 2020, Day 13, Part 2

https://adventofcode.com/2020/day/13

Given a list of buses and the cycle intervals they depart, calculate the
earliest time where they would each depart at the offsets matching their
positions in the list.

This is tricky to do with closed-form math, but an algorithm that tracks
the repeating cycle when adding each bus, and then looping through the
cycles when adding a new bus until it fits the pattern gives an efficient
solution.

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

        bus_list = []
        for idx in range(len(buses)):
            if buses[idx] == 'x':
                continue
            bus_list.append({ 'ts': idx, 'bus_num': int(buses[idx]) })

    # The tricky part about this is that the remainders have to
    # line up with a time offset. This is very tricky to do mathematically
    # so the strategy is to take each bus, and figure out the cycle time
    # when each new bus number is added. Note each bus number is a prime
    # number.
    #
    # Then given the cycle, start at the minimum time stamp and loop through
    # cycles until the new bus's modulo is zero. Update the total cycle to
    # reflect the new bus's cycle time and repeat.
    ts = 0
    cycle = 0
    base = 0
    for bus in bus_list:
        # Initialize first
        if cycle == 0:
            cycle = bus['bus_num']
            base = 0
            continue

        bus_num = bus['bus_num']
        offset = bus['ts']
        for cycle_num in range(0, 999):
            new_ts = base + cycle_num * cycle
            m = (new_ts + offset) % bus_num
            if m == 0:
                break

        ts = new_ts
        cycle *= bus_num
        base = ts % cycle

    return ts

answer = main()
print(f"Answer is {answer}")
