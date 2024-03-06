#!/usr/bin/python
"""Advent of Code 2020, Day 24, Part 2

https://adventofcode.com/2020/day/24

For a grid of hexagonal tiles, follow a path of directions and flip the
color of the tile at the end between white to black. Then perform rules
of flipping tiles based on the number of adjacent black tiles. Figure out
the final number of black tiles at the end.

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

# List of tuples with coordinates of black tiles
tiles_flipped = set()

# Array of moves for the hexagonal coordinates
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

# Process the moves like Part 1
def process_moves(moves):
    cur_x, cur_y, idx = 0, 0, 0
    while idx < len(moves):
        width = 2 if moves[idx] in ('s', 'n') else 1
        cur_x, cur_y = move_dir(cur_x, cur_y, moves[idx:idx+width])
        idx += width

    # Add to set if now black, remove from set if now white
    key = (cur_x, cur_y)
    if key in tiles_flipped:
        tiles_flipped.remove(key)
    else:
        tiles_flipped.add(key)

# Perform the flipping rules for one cycle
def flip_tiles():
    # Figure out range of tiles
    x_low, x_high = 9999, 0
    y_low, y_high = 9999, 0
    for key in tiles_flipped:
        x_low, x_high = min(x_low, key[0]), max(x_high, key[0])
        y_low, y_high = min(y_low, key[1]), max(y_high, key[1])
    x_low, x_high = x_low-1, x_high+1
    y_low, y_high = y_low-1, y_high+1

    to_black, to_white = [], []
    for y in range(y_low, y_high+1):
        for x in range(x_low, x_high+1):
            # How many adjacent black tiles?
            num_black_adj = 0
            for d in ('e', 'w', 'nw', 'ne', 'sw', 'se'):
                num_black_adj += move_dir(x, y, d) in tiles_flipped

            if (x, y) in tiles_flipped:     # If tile is black
                if num_black_adj == 0 or num_black_adj > 2:
                    to_white.append((x, y))
            else:
                if num_black_adj == 2:
                    to_black.append((x, y))

    for x, y in to_white:
        tiles_flipped.remove((x, y))
    for x, y in to_black:
        tiles_flipped.add((x, y))

def main():
    with open(fn, 'r') as file:
        for line in file:
            process_moves(line.rstrip('\n'))

    for day in range(1, 101):
        flip_tiles()

    return len(tiles_flipped)

answer = main()
print(f"Answer is {answer}")
