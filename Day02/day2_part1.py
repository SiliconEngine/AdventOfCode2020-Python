#!/usr/bin/python
"""Advent of Code 2020, Day 2, Part 1

https://adventofcode.com/2020/day/2

Parse a "password rule" policy and determine if each line is correct.
Display how many pass the rule.

See test.dat for sample data and prod.dat for full data.

Author: Tim Behrendsen
"""

fn = 'prod.dat'

with open(fn, 'r') as file:
    content = file.read()

lines = content.split("\n")
correct = 0
for line in lines:
    if (line == ""):
        continue
    
    dt = line.split()
    r = dt[0].split('-')
    r1 = int(r[0])
    r2 = int(r[1])
    letter = dt[1][0]

    count = 0
    for c in dt[2]:
        if c == letter:
            count += 1

    # Count of the given letter must be within given range
    if count >= r1 and count <= r2:
        correct += 1

print(f"Number correct is {correct}")
