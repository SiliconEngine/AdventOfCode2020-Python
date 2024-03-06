#!/usr/bin/python
"""Advent of Code 2020, Day 1, Part 1

https://adventofcode.com/2020/day/1

Given a list of numbers, find the two that total to 2020.

See test.dat for sample data and prod.dat for full data.

Author: Tim Behrendsen
"""

fn = 'prod.dat'

with open(fn, 'r') as file:
    content = file.read()

lines = content.split()
num_list = [ float(num) for num in lines ]

for i1 in range(len(num_list)-1):
    for i2 in range(i1+1, len(num_list)):
        if num_list[i1] + num_list[i2] == 2020:
            print(num_list[i1])
            print(num_list[i2])
            print(num_list[i1] * num_list[i2])

