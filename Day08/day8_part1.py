#!/usr/bin/python
"""Advent of Code 2020, Day 8, Part 1

https://adventofcode.com/2020/day/8

Given a list of program instructions (nop, jmp and acc), follow the
instructions and terminate when the same instruction is executed twice.
Show the final accumulator value.

See test.dat for sample data and program.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'program.dat'

import re

def main():
    # Read in program data
    program = []
    with open(fn, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break

            line = line.rstrip("\n")
            pair = line.split(' ')
            opcode = pair[0]
            value = int(pair[1])
            program.append((opcode, value))

    # Run the program
    pc = 0
    acc = 0
    executed = set()
    while True:
        inst = program[pc]
        executed.add(pc)
        opcode = inst[0]
        if opcode == 'nop':
            pc += 1
        elif opcode == 'acc':
            acc += inst[1]
            pc += 1
        elif opcode == 'jmp':
            pc += inst[1]

        if pc in executed:
            break

    return acc

total = main()
print(f"Accumulator is {total}")
