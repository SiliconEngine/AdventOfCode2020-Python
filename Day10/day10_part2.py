#!/usr/bin/python
"""Advent of Code 2020, Day 10, Part 2

https://adventofcode.com/2020/day/10

Give a list of "joltages" for a group of adapters, determine the number
of combinations of adapters that convert 0 jolts to the final number.
An adapter can increase the joltages only a maximum of three.

Recursive algorithm that uses dynamic programming to solve the problem
quickly by caching intermediate results.

See test.dat and test2.dat for sample data and adapters.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'test2.dat'
fn = 'adapters.dat'

import re

# Cache of how many combinations are at an index
cache = { }

def find_combos(num_list, idx = 0):
    global cache

    # If hit end, then count this as one
    if idx == len(num_list)-1:
        return 1

    # See if we've cached the number of combinations at this index
    c = cache.get(idx)
    if c != None:
        return c

    # Search for adapters that are less than three and recursively
    # check each path
    n = num_list[idx]
    count = 0
    for new_idx in range(idx+1, len(num_list)):
        if num_list[new_idx] - n > 3:
            break
        new_count = find_combos(num_list, new_idx)
        count += new_count

        # Cache the amount we found past this point, which will be the
        # same no matter what came before
        c = cache.get(new_idx)
        if c != None and c != new_count:
            raise Exception(f"NEW TOTAL ({new_idx}) from {c} to {new_count}")
        cache[new_idx] = new_count

    return count

def main():
    # Read in number list
    with open(fn, 'r') as file:
        num_list = [ int(line.rstrip("\n")) for line in file ]

    # Don't need the device jolt for part 2, because the end of the list must
    # be last number, since the device jolt is three past it.
    device_jolt = max(num_list) + 3

    # Add the starting zero jolt at the front
    num_list.insert(0, 0)
    num_list.sort()

    count = find_combos(num_list)
    return count

answer = main()
print(f"Answer is {answer}")
