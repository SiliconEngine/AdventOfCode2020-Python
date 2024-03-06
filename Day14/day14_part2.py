#!/usr/bin/python
"""Advent of Code 2020, Day 14, Part 2

https://adventofcode.com/2020/day/14

Given input data of a mask and setting memory locations, apply the mask
to the memory location before assignment. The wrinkle is that if there is
an 'X' in the mask, then that counts as either a 0 or a 1, and both memory
locations are assigned. Once all assigned, add up all the numbers.

The number of potential memory locations was small enough that just
unpacking all the addresses work reasonably.

See test2.dat for sample data and program.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test2.dat'
fn = 'program.dat'

import re

def apply_mask(mask, addr):
    bit = 1
    for idx in range(-1, -37, -1):
        c = mask[idx]
        if c == '0':
            pass        # Unchanged
        elif c == '1':
            addr |= bit
        else:           # For an 'X', just zero it out
            addr &= ~bit


        bit <<= 1

    num_x = mask.count('X')
    combo_range = 2 ** num_x

    addr_list = []
    for combo_n in range(combo_range):
        xpos = len(mask)
        new_addr = addr
        for combo_bit in range(num_x):
            xpos = mask.rfind('X', 0, xpos)

            combo_mask = (1 << combo_bit)
            x_mask = (1 << (35-xpos))
            # Note bits at 'X' positions are already zero
            if combo_n & (1 << combo_bit):
                new_addr |= x_mask         # Set to 1

        addr_list.append(new_addr)

    return addr_list

def main():
    memory = {}
    cur_mask = None

    total = 0
    with open(fn, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            line = line.rstrip("\n")
            matches = re.findall(r'(.*) = (.*)', line)

            op = matches[0][0]
            param = matches[0][1]
            if op == 'mask':
                cur_mask = param

            else:
                matches = re.findall(r'\d+', op)
                addr = int(matches[0])
                num = int(param)

                addr_list = apply_mask(cur_mask, addr)
                for new_addr in addr_list:
                    memory[new_addr] = num

    count = 0
    for n in memory.values():
        total += n

    return total

answer = main()
print(f"Answer is {answer}")
