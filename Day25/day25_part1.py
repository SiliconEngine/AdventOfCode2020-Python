#!/usr/bin/python
"""Advent of Code 2020, Day 24, Part 1

https://adventofcode.com/2020/day/24

Given a set of "public keys", determine the private key using the supplied
algorithm. This is pretty much just an easy brute-force problem.

See test.dat for sample data and keys.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'keys.dat'

import re

def calc_value(subject_num, loop_size):
    value = 1
    for loop in range(loop_size):
        value = (value * subject_num) % 20201227
    return value

def main():
    count = 0
    with open(fn, 'r') as file:
        card_key = int(file.readline().rstrip('\n'))
        door_key = int(file.readline().rstrip('\n'))

    # Search for loop count for card
    value, loop_size = 1, 0
    while value != card_key:
        value = (value * 7) % 20201227
        loop_size += 1
    card_loop = loop_size

    # Search for loop count for door (technically not needed)
    value, loop_size = 1, 0
    while value != door_key:
        value = (value * 7) % 20201227
        loop_size += 1
    door_loop = loop_size

    # Calc both, just to be sure it's correct
    v1 = calc_value(door_key, card_loop)
    v2 = calc_value(card_key, door_loop)
    if v1 != v2:
        raise Exception("Got non-matching values {v1} and {v2}")

    return v1

answer = main()
print(f"Answer is {answer}")
