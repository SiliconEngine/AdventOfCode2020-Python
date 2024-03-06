#!/usr/bin/python
"""Advent of Code 2020, Day 12, Part 1

https://adventofcode.com/2020/day/12

Given a set of ship movement instructions, determine the final
position of the ship.

See test.dat for sample data and moves.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'moves.dat'

import re

turns = {
    'R90': { 'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E' },
    'L90': { 'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E' },
    'R180': { 'E': 'W', 'W': 'E', 'N': 'S', 'S': 'N' },
    'L180': { 'E': 'W', 'W': 'E', 'N': 'S', 'S': 'N' },
    'R270': { 'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E' },
    'L270': { 'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E' },
}

def main():
    # Read in moves
    cur_y = 0
    cur_x = 0
    cur_dir = 'E'
    with open(fn, 'r') as file:
        for line in file:
            line = line.rstrip("\n")
            move = line[0]
            num = int(line[1:])
            if move in ('N', 'S', 'E', 'W'):
                move_dir = move
            elif move in ('R', 'L'):
                cur_dir = turns[line][cur_dir]
                move_dir = cur_dir
                num = 0
            else:
                move_dir = cur_dir

            if move_dir == 'W':
                cur_x -= num
            elif move_dir == 'E':
                cur_x += num
            elif move_dir == 'N':
                cur_y -= num
            elif move_dir == 'S':
                cur_y += num

    return abs(cur_x) + abs(cur_y)

answer = main()
print(f"Answer is {answer}")
