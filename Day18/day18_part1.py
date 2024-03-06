#!/usr/bin/python
"""Advent of Code 2020, Day 18, Part 1

https://adventofcode.com/2020/day/18

Simple expression evaluator that doesn't use precedence.

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

    stack = []

    n = None
    for t in tokens:
        if t.isdigit():
            stack.append(int(t))
        else:
            stack.append(t)

        while True:
            peek = stack[-1]
            if peek == '(' or peek in ('+', '*'):
                break

            if isinstance(peek, int):
                if len(stack) == 1:
                    break
                if stack[-2] == '(':
                    break

            if peek == ')':
                n2 = None
                stack.pop()
                while True:
                    t2 = stack.pop()
                    if t2 == '(':
                        break
                    elif isinstance(t2, int):
                        n2 = t2
                    else:
                        raise Exception(f"Unexpected {t2} pop parens")
                stack.append(n2)
                continue

            # Must be ready for operator
            n2 = stack.pop()
            op = stack.pop()
            n = stack.pop()
            if op == '*':
                n *= n2
            elif op == '+':
                n += n2
            stack.append(n)

    return stack.pop()

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
