#!/usr/bin/python
"""Advent of Code 2020, Day 18, Part 2

https://adventofcode.com/2020/day/18

Expression evaluator that uses opposite precedence from the norm, where '+'
has higher precedence than '*'. Uses two-stack algorithm for eval.

See test.dat for sample data and expr.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'expr.dat'

import re

def eval(expr):
    # Split on spaces and parentheses, then need to eliminate the spaces
    tokens = re.split(r'(\s|\(|\))', expr)
    tokens = [ t for t in tokens if t.rstrip(' ') != '' ]

    op_stack = []
    num_stack = []

    # Do operation at top of stack
    def do_eval():
        op = op_stack.pop()
        n1 = num_stack.pop()
        n2 = num_stack.pop()
        if op == '+':
            num_stack.append(n1 + n2)
        elif op == '*':
            num_stack.append(n1 * n2)

    # Process each token
    for t in tokens:
        if t.isdigit():
            num_stack.append(int(t))
        elif t in ('+', '*'):
            while True:
                if len(op_stack) == 0:
                    op_stack.append(t)
                    break

                peek = op_stack[-1]

                # Check higher precedence
                if peek == '(' or (t == '+' and peek == '*'):
                    op_stack.append(t)
                    break

                do_eval()

        elif t == '(':
            op_stack.append(t)

        elif t == ')':
            while op_stack[-1] != '(':
                do_eval()
            op_stack.pop()

    # Do final unwind
    while len(num_stack) > 1:
        do_eval()

    return num_stack[0]

def main():
    with open(fn, 'r') as file:
        total = 0
        for line in file:
            line = line.rstrip("\n")
            n = eval(line)
            total += n

    return total

answer = main()
print(f"Answer is {answer}")
