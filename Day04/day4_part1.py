#!/usr/bin/python
"""Advent of Code 2020, Day 4, Part 1

https://adventofcode.com/2020/day/4

Given a list of passport fields, determine how many have all required
fields.

See test.dat for sample data and keys.dat for full data.

Author: Tim Behrendsen
"""

fn = 'prod.dat'

req_list = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" ] #, "cid" ]

with open(fn, 'r') as file:
    content = file.read()
lines = content.split("\n")

p = {}
pp_list = []
for line in lines:
    if line == '':
        pp_list.append(p)
        p = {}

    fields = line.split();
    for f in fields:
        kv = f.split(':')
        p[kv[0]] = kv[1]

val_count = 0
for pp in pp_list:
    fld_list = list(pp.keys())
    is_valid = True
    for req in req_list:
        if not req in fld_list:
            is_valid = False

    val_count += is_valid

print(f"valid count is {val_count}")
