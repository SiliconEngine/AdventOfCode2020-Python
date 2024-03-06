#!/usr/bin/python
"""Advent of Code 2020, Day 15, Part 2

https://adventofcode.com/2020/day/15

Simulate elf memory game, doing 30,000,000 rounds.

See test.dat for sample data and numbers.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'numbers.dat'

import re

def main():
    turn_track = { }

    with open(fn, 'r') as file:
        line = file.readline()
        line = line.rstrip("\n")
        init_nums = [ int(n) for n in line.split(',') ]

    turn = 0
    for num in init_nums:
        turn += 1
        turn_track[num] = [ turn ]
        last_num = num

    was_first = True
    while turn < 30000000:
        turn += 1

        if was_first:
            new_num = 0
        else:
            new_num = turn_track[last_num][1] - turn_track[last_num][0]

        track = turn_track.get(new_num)
        if track == None:
            was_first = True
            turn_track[new_num] = [ turn ]
        else:
            was_first = False
            track.append(turn)
            if len(track) > 2:
                del track[0]

        last_num = new_num

    return new_num

answer = main()
print(f"Answer is {answer}")
