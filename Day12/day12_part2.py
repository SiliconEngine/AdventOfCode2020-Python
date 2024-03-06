#!/usr/bin/python
"""Advent of Code 2020, Day 12, Part 2

https://adventofcode.com/2020/day/12

Given a set of movement instructions, some for a ship's position, and some
for a "waypoint", determine the ship's final position as it follows the
waypoint.

See test.dat for sample data and moves.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'moves.dat'

import re

def main():
    # Read in moves
    ship_x = 0
    ship_y = 0
    wayp_x = 10
    wayp_y = -1
    ship_dir = 'E'
    with open(fn, 'r') as file:
        for line in file:
            line = line.rstrip("\n")
            move = line[0]
            num = int(line[1:])
            wayp_move = None
            ship_move = None

            if move in ('N', 'S', 'E', 'W'):
                if move == 'W':
                    wayp_x -= num
                elif move == 'E':
                    wayp_x += num
                elif move == 'N':
                    wayp_y -= num
                elif move == 'S':
                    wayp_y += num

            elif move == 'F':
                ship_x = ship_x + num * wayp_x
                ship_y = ship_y + num * wayp_y

            elif move == 'R':
                for i in range(num // 90):
                    wayp_x, wayp_y = 0-wayp_y, wayp_x

            elif move == 'L':
                for i in range(num // 90):
                    wayp_x, wayp_y = wayp_y, 0-wayp_x

    return abs(ship_x) + abs(ship_y)

answer = main()
print(f"Answer is {answer}")
