#!/usr/bin/python
"""Advent of Code 2020, Day 1, Part 2

https://adventofcode.com/2020/day/1

Given a list of number, find the three that total to 2020.

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
        for i3 in range(i2+1, len(num_list)):
            if num_list[i1] + num_list[i2] + num_list[i3] == 2020:
                print(num_list[i1])
                print(num_list[i2])
                print(num_list[i3])
                print(num_list[i1] * num_list[i2] * num_list[i3])

