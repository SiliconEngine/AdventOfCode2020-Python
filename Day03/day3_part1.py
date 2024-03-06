#!/usr/bin/python
"""Advent of Code 2020, Day 3, Part 1 and Part 2

https://adventofcode.com/2020/day/3

Input: a map of a slope and trees.
Part 1: How many trees are encountered traversing right 3 and down 1.
Part 2: Similar, but use five different slope numbers.

See prod.dat for full data.

Author: Tim Behrendsen
"""

fn = 'prod.dat'

def calc(offset_y, offset_x):
    x = y = 0
    count = 0

    while True:
        x += offset_x
        if x >= cols:
            x -= cols
        y += offset_y
        if y >= rows:
            break
        if map[y][x] == "#":
            count += 1

    return count

with open(fn, 'r') as file:
    content = file.read()

map = content.split("\n")
map.pop()
rows = len(map)
cols = len(map[0])
count1 = calc(1, 1)
count2 = calc(1, 3)
count3 = calc(1, 5)
count4 = calc(1, 7)
count5 = calc(2, 1)

print(f"Part 1 is {count2}")

count = count1 * count2 * count3 * count4 * count5;
print(f"Part 2 is {count}")
