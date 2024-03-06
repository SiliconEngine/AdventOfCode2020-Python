#!/usr/bin/python
"""Advent of Code 2020, Day 8, Part 2

https://adventofcode.com/2020/day/8

Given a list of program instructions (nop, jmp and acc), follow the
instructions, but there is one instruction that has to either be changed
from a jmp->nop, or a nop->jmp, in order to execute the last instruction.
Otherwise, will go into a loop.

See test.dat for sample data and program.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'program.dat'

import re

def run_program(program):
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

        # If same instruction done twice, then loop
        if pc in executed:
            break

        # If final instruction, we're successful
        if pc == len(program):
            return acc

    return None

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
            program.append([opcode, value])

    for inst in program:
        # Test each instruction by changing nop->jmp or jmp->nop
        if inst[0] == 'nop':
            inst[0] = 'jmp'
            acc = run_program(program)
            if acc != None:
                break
            inst[0] = 'nop'

        elif inst[0] == 'jmp':
            inst[0] = 'nop'
            acc = run_program(program)
            if acc != None:
                break
            inst[0] = 'jmp'

    return acc

total = main()
print(f"Accumulator is {total}")
