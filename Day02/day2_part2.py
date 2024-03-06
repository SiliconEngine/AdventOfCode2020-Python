#!/usr/bin/python
"""Advent of Code 2020, Day 2, Part 2

https://adventofcode.com/2020/day/2

Parse a "password rule" policy and determine if each line is correct.
Display how many pass the rule. Slightly more complicated rule in Part 2.

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
    pwd = dt[2]
    # Exactly one of the positions must contain the given letter.
    if ((r1 <= len(pwd) and pwd[r1-1] == letter) ^ (r2 <= len(pwd) and pwd[r2-1] == letter)):
        correct += 1

print(f"Number correct is {correct}")
