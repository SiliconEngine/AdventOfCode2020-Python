#!/usr/bin/python
"""Advent of Code 2020, Day 9, Part 1

https://adventofcode.com/2020/day/9

Give a list of numbers, identify which number is not a sum of two of the prior
numbers in a certain window size (5 in the test, 25 in the full data set).

See test.dat for sample data and xmas_data.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
window_size = 5

fn = 'xmas_data.dat'
window_size = 25

import re

def main():
    # Read in number list
    num_list = []
    with open(fn, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break

            line = line.rstrip("\n")
            num_list.append(int(line))

    # We'll use a hash of what sums we had before, and add/remove
    # as we go. Brute force probably would have been find for this
    # problem, but this will be fast.
    chk_hash = { }

    # Initialize the hash with the first (window_size) numbers
    for idx1 in range(0, window_size-1):
        for idx2 in range(idx1+1, window_size):
            n1 = num_list[idx1]
            n2 = num_list[idx2]
            if n1 == n2:
                continue
            key = n1 + n2
            chk_hash[key] = chk_hash.get(key, 0) + 1

    # Check the numbers past initial numbers
    for test_idx in range(window_size, len(num_list)):
        n = num_list[test_idx]
        count = chk_hash.get(num_list[test_idx])
        if count == None or count == 0:
            break

        # Remove numbers outside the prior window
        rmv_idx = test_idx - window_size
        n1 = num_list[rmv_idx]
        for idx in range(rmv_idx+1, rmv_idx+window_size):
            n2 = num_list[idx]
            if n1 == n2:
                continue
            key = n1 + n2
            chk_hash[key] -= 1

        # Add numbers now in the prior window
        n1 = n
        for idx in range(test_idx-window_size, test_idx):
            n2 = num_list[idx]
            if n1 == n2:
                continue
            key = n1 + n2
            chk_hash[key] = chk_hash.get(key, 0) + 1

    return n

answer = main()
print(f"Answer is {answer}")
