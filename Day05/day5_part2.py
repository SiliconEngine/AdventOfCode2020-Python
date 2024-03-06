#!/usr/bin/python
"""Advent of Code 2020, Day 5, Part 2

https://adventofcode.com/2020/day/5

An airline uses a "binary space partition" seating arrangement, where you
get "F"(front) or "B"(back) letters to divide the seating rows, then 
"L" or "R" to divide the row to determine the seat. Convert the letters
to seat numbers. Identify a seat missing from the list, with the caveat
that seats at the front and back are missing, so the one we want is in
the middle.

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

seats = {}
for line in lines:
    (row, col) = calc(line)
    seat = row * 8 + col
    seats[seat] = 'X'

# Look for missing seat among taken seats
last_missing = -1
seat_id = None
for i in range(128 * 8):
    if seats.get(i) == None:
        if last_missing > 0 and (i - last_missing) > 1:
            if seats.get(i+1) != None:
                seat_id = i
                break
        last_missing = i

print(seat_id)
