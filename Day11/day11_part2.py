#!/usr/bin/python
"""Advent of Code 2020, Day 11, Part 2

https://adventofcode.com/2020/day/11

Given a map of seats, apply rules of people being seated / unseated.
Continue until the map no longer changes. For part 2, need to scan
along rows/columns to determine the rule.

See test.dat for sample data and seats.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'seats.dat'

import re

def sign(n):
    return (n > 0) - (n < 0)

class Seat:
    def __init__(self, row, col, c):
        self.row = row
        self.col = col
        self.c = c
        self.new_c = None

class SeatMap:
    def __init__(self, seat_map):
        self.seat_map = seat_map
        self.num_rows = len(seat_map)
        self.num_cols = len(seat_map[0])

    def get_c(self, row, row_dir, col, col_dir):
        while True:
            if row < 0 or row >= self.num_rows:
                return '.'
            if col < 0 or col >= self.num_cols:
                return '.'
            c = self.seat_map[row][col].c
            if c != '.':
                return c
            row += row_dir
            col += col_dir

    def dump(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.seat_map[row][col].c, end = '')
            print()

    def apply_rules(self):
        for row_list in self.seat_map:
            for node in row_list:
                c = node.c
                row = node.row
                col = node.col
                if c == 'L':
                    # Rule: If no occupied seats next to this one,
                    # then becomes occupied
                    brk = False
                    for r in range(row-1, row+2):
                        for c in range(col-1, col+2):
                            if r == row and c == col:
                                continue
                            c2 = self.get_c(r, sign(r - row), c, sign(c - col))
                            if c2 == '#':
                                brk = True
                                break
                        if (brk):
                            break

                    node.new_c = 'L' if brk else '#'

                elif c == '#':
                    # Rule: If four or more adjacent seats occupied,
                    # then becomes empty
                    brk = False
                    count = 0
                    for r in range(row-1, row+2):
                        for c in range(col-1, col+2):
                            if r == row and c == col:
                                continue
                            c2 = self.get_c(r, sign(r - row), c, sign(c - col))
                            if c2 == '#':
                                count += 1
                                if count == 5:
                                    brk = True
                                    break
                        if (brk):
                            break

                    node.new_c = 'L' if brk else '#'

        num_occupied = 0
        num_changed = 0
        for row_list in self.seat_map:
            for node in row_list:
                if node.c != '.':
                    if node.c != node.new_c:
                        num_changed += 1

                    node.c = node.new_c
                    if node.c == '#':
                        num_occupied += 1

        return num_occupied, num_changed


def main():
    # Read in seat map
    seat_rows = []
    with open(fn, 'r') as file:
        row = 0
        for line in file:
            line = line.rstrip("\n")
            col = 0
            seat_row = [ ]
            for c in line:
                seat = Seat(row, col, c)
                seat_row.append(seat)
                col += 1

            seat_rows.append(seat_row)
            row += 1

    seat_map = SeatMap(seat_rows)

    num_changed = -1
    while num_changed:
        num_occupied, num_changed = seat_map.apply_rules()

    return num_occupied

answer = main()
print(f"Answer is {answer}")
