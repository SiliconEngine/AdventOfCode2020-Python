#!/usr/bin/python
"""Advent of Code 2020, Day 23, Part 2

https://adventofcode.com/2020/day/23

Given a set up of nine cups in a circle labeled 1-9, along with more cups
from 10 through 1,000,000, move them according to a set of rules and
determine the final layout, but we're doing 10,000,000 moves.

Requires an efficient data structure, but overall needed to be brute force.

See test.dat for sample data and cups.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'cups.dat'

import re

class Node:
    def __init__(self, content):
        self.content = content
        self.back = None
        self.fwd = None

    def __repr__(self):
        b = "None" if self.back == None else self.back.content
        f = "None" if self.fwd == None else self.fwd.content
        return f"[{self.content}: back={b}, fwd={f}]"

class Ring:
    def __init__(self):
        self.ring = None
        self.cache = { }

    def add(self, node):
        self.cache[node.content] = node
        if self.ring == None:
            self.ring = node
            node.back = node
            node.fwd = node
            return

        self.move(node)
        return

    def move(self, node):
        fwd = self.ring.fwd
        node.back = self.ring
        node.fwd = fwd
        fwd.back = node
        self.ring.fwd = node

        self.ring = node
        return

    def peek_cur(self):
        return self.ring

    def delete(self, node):
        fwd = node.fwd
        node.back.fwd = node.fwd
        fwd.back = node.back
        node.fwd = None
        node.back = None
        return

    def get_cur(self):
        node = self.ring
        self.ring = node.fwd
        self.delete(node)
        return node

    def move_bwd(self):
        self.ring = self.ring.back

    def move_fwd(self):
        self.ring = self.ring.fwd

    def find_item(self, item):
        node = self.cache[item]
        if node.fwd == None:
            return False
        self.ring = node
        return True

    def get_state(self):
        node = self.cache[1]
        v1 = node.fwd.content
        v2 = node.fwd.fwd.content
        return f"[{v1} / {v2} / {v1 * v2}]"

    def __repr__(self):
        items = []
        cur_node = self.ring
        max_count = 20
        while True:
            items.append(cur_node.content)
            cur_node = cur_node.fwd
            max_count -= 1
            if cur_node == self.ring or max_count == 0:
                break

        return f"[ring:{', '.join([ str(i) for i in items ])}]"

def main():
    with open(fn, 'r') as file:
        cups = file.readline().rstrip('\n')

    #print(cups)
    ring = Ring()
    max_cup = 9
    min_cup = 1
    for c in cups:
        c = int(c)
        ring.add(Node(c))

    for i in range(10, 1000001):
        ring.add(Node(i))
    max_cup = 1000000

    ring.find_item(int(cups[0]))

    for move in range(10000000):
        cur_cup = ring.peek_cur()

        ring.move_fwd()
        holder1 = ring.get_cur()
        holder2 = ring.get_cur()
        holder3 = ring.get_cur()
        ring.move_bwd()

        srch_cup = cur_cup.content
        while True:
            srch_cup -= 1
            if srch_cup < min_cup:
                srch_cup = max_cup
            if ring.find_item(srch_cup):
                break

        ring.move(holder1)
        ring.move(holder2)
        ring.move(holder3)

        ring.find_item(cur_cup.content)
        ring.move_fwd()

    return ring.get_state()

answer = main()
print(f"Answer is {answer}")
