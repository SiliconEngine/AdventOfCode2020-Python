#!/usr/bin/python
"""Advent of Code 2020, Day 5, Part 1

https://adventofcode.com/2020/day/5

An airline uses a "binary space partition" seating arrangement, where you
get "F"(front) or "B"(back) letters to divide the seating rows, then 
"L" or "R" to divide the row to determine the seat. Convert the letters
to seat numbers and identify the highest seat.

See test.dat for sample data and prod.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'prod.dat'

def calc(p):
    low = 0
    high = 127
    for n in range(7):
        mid = int((low+high+1) / 2) - 1
        fb = p[n]
        if fb == "F":
            high = mid
        elif fb == "B":
            low = mid+1
        else:
            print(f"BAD, fb = {fb}")
            exit(0)

    row = low

    low = 0
    high = 7
    for n in range(7, 10):
        mid = int((low+high+1) / 2) - 1
        rl = p[n]
        if rl == "L":
            high = mid
        elif rl == "R":
            low = mid+1
        else:
            print(f"BAD, rl = {rl}")
            exit(0)

    col = low

    return [ row, col ]

with open(fn, 'r') as file:
    content = file.read()

lines = content.split("\n")
lines.pop()
high_seat = 0

for line in lines:
    (row, col) = calc(line)
    seat = row * 8 + col
    if seat > high_seat:
        high_seat = seat

print(f"high_seat = {high_seat}")

