#!/usr/bin/python
"""Advent of Code 2020, Day 24, Part 1

https://adventofcode.com/2020/day/24

For a grid of hexagonal tiles, follow a path of directions and flip the
color of the tile at the end between white to black. Figure out the number
of black tiles at the end.

Flat side is East-West. Uses a coordinate system like:

[0,0]  [2,0]  [4,0]
   [1,0]  [3,0]  [5,0]
[0,1]  [2,1]  [4,1]
   [1,1]  [3,1]  [5,1]

See test.dat for sample data and tiles.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'tiles.dat'

import re

tiles_flipped = { }

dir_moves = {
    # Even x value       Odd x value
    ('e', 0): (2, 0),    ('e', 1): (2, 0),
    ('w', 0): (-2, 0),   ('w', 1): (-2, 0),
    ('nw', 0): (-1, -1), ('nw', 1): (-1, 0),
    ('ne', 0): (1, -1),  ('ne', 1): (1, 0),
    ('sw', 0): (-1, 0),  ('sw', 1): (-1, 1),
    ('se', 0): (1, 0),   ('se', 1): (1, 1),
}

def move_dir(x, y, d):
    offsets = dir_moves[(d, x % 2)]
    return (x + offsets[0], y + offsets[1])

def process_moves(moves):
    cur_x = 0
    cur_y = 0

    idx = 0
    while idx < len(moves):
        move = moves[idx]
        if move == 's' or move == 'n':
            idx += 1
            move += moves[idx]
        idx += 1
        cur_x, cur_y = move_dir(cur_x, cur_y, move)

    key = f"{cur_x},{cur_y}"
    tiles_flipped.setdefault(key, 0)
    tiles_flipped[key] += 1

def main():
    count = 0
    with open(fn, 'r') as file:
        for line in file:
            moves = line.rstrip('\n')

            process_moves(moves)
            count += 1

    # Count number of black tiles (flipped an odd number of times)
    black_count = 0
    for key, count in tiles_flipped.items():
        if (count % 2) != 0:
            black_count += 1

    return black_count

answer = main()
print(f"Answer is {answer}")
