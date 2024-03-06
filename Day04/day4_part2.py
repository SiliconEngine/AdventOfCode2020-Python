#!/usr/bin/python
"""Advent of Code 2020, Day 4, Part 2

https://adventofcode.com/2020/day/4

Given a list of field validation rules for a list of passports, determine
number of valid ones.

See test.dat for sample data and keys.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'prod.dat'

req_list = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" ] #, "cid" ]

with open(fn, 'r') as file:
    content = file.read()
lines = content.split("\n")

p = {}
pp_list = []
for line in lines:
    if (line == ""):
        pp_list.append(p)
        p = {}

    fields = line.split();
    for f in fields:
        kv = f.split(':')
        p[kv[0]] = kv[1]

inv_count = 0
for pp in pp_list:
    bad = False
    for chk in req_list:
        if (pp.get(chk) == None):
            bad = True
            break;

    if not bad:
        byr = pp['byr']
        if not (byr.isdigit() and int(byr) >= 1920 and int(byr) <= 2002):
            bad = True

    if not bad:
        iyr = pp['iyr']
        if not (iyr.isdigit() and int(iyr) >= 2010 and int(iyr) <= 2020):
            bad = True

    if not bad:
        eyr = pp['eyr']
        if not (eyr.isdigit() and int(eyr) >= 2020 and int(eyr) <= 2030):
            bad = True

    if not bad:
        hgt = pp['hgt']
        sfx = hgt[-2:]
        hgt = hgt[0:-2]
        if not hgt.isdigit():
            bad = True
        elif sfx != "cm" and sfx != "in":
            bad = True
        elif sfx == "cm" and not (int(hgt) >= 150 and int(hgt) <= 193):
            bad = True
        elif sfx == "in" and not (int(hgt) >= 59 and int(hgt) <= 76):
            bad = True

    if not bad:
        hcl = pp['hcl']
        if re.search("^#[0-9a-f]{6}$", hcl) == None:
            bad = True

    if not bad:
        ecl = pp['ecl']
        if re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", ecl) == None:
            bad = True

    if not bad:
        pid = pp['pid']
        if re.search("^\d{9}$", pid) == None:
            bad = True

    if bad:
        inv_count += 1

val_count = len(pp_list) - inv_count
print(f"valid count is {val_count}")
