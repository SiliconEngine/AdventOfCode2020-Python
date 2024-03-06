#!/usr/bin/python
"""Advent of Code 2020, Day 23, Part 1

https://adventofcode.com/2020/day/23

Given a set up of nine cups in a circle labeled 1-9, move them according
to a set of rules and after 100 iterations, determine the final layout.

See test.dat for sample data and cups.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'cups.dat'

import re

class Ring:
    def __init__(self):
        self.ring = []
        self.cur_pos = -1

    def add(self, item):
        self.cur_pos += 1
        self.ring.insert(self.cur_pos, item)

    def set_cur(self, idx):
        self.cur_pos = idx

    def peek_cur(self):
        return self.ring[self.cur_pos]

    def get_cur(self):
        item = self.ring[self.cur_pos]
        del self.ring[self.cur_pos]
        if self.cur_pos >= len(self.ring):
            self.cur_pos = 0
        return item

    def move_bwd(self):
        self.cur_pos -= 1
        if self.cur_pos < 0:
            self.cur_pos = len(self.ring)-1

    def move_fwd(self):
        self.cur_pos += 1
        if self.cur_pos == len(self.ring):
            self.cur_pos = 0

    def find_item(self, item):
        try:
            new_pos = self.ring.index(item)
            self.cur_pos = new_pos
            return True
        except ValueError:
            return False

    def get_state(self):
        cup_one = self.ring.index(1)
        return ''.join([ str(self.ring[(i + cup_one + 1) % len(self.ring)]) for i in range(len(self.ring)-1) ])

    def __repr__(self):
        return f"[pos:{self.cur_pos}, ring:{self.ring}]"


def main():
    with open(fn, 'r') as file:
        cups = file.readline().rstrip('\n')

    ring = Ring()
    max_cup = 0
    min_cup = 10
    for c in cups:
        c = int(c)
        ring.add(c)
        if c > max_cup:
            max_cup = c
        if c < min_cup:
            min_cup = c
    ring.find_item(int(cups[0]))

    for move in range(100):
        cur_cup = ring.peek_cur()
        ring.move_fwd()

        holder = []
        for i in range(3):
            holder.append(ring.get_cur())

        ring.move_bwd()
        srch_cup = cur_cup
        while True:
            srch_cup -= 1
            if srch_cup < min_cup:
                srch_cup = max_cup
            if ring.find_item(srch_cup):
                break

        for cup in holder:
            ring.add(cup)

        ring.find_item(cur_cup)
        ring.move_fwd()

    return ring.get_state()

answer = main()
print(f"Answer is {answer}")
