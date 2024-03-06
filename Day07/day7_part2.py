#!/usr/bin/python
"""Advent of Code 2020, Day 7, Part 2

https://adventofcode.com/2020/day/7

Given a set of rules about how many specific colored bags can be
contained within a different bag, figure out how many bags can be
contained within one shiny gold bag, with nesting allowed.

See test.dat for sample data and answers.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test2.dat'
fn = 'rules.dat'

import re

class Bag:
    def __init__(self, name):
        self.contains = []
        self.within = []
        self.name = name

    def add_contains(self, count, bag):
        self.contains.append([int(count), bag ])

    def add_within(self, count, bag):
        self.within.append([int(count), bag ])

    def __repr__(self):
        s1 = ', '.join([ f"{c[0]} {c[1].name}" for c in self.contains ])
        s2 = ', '.join([ f"{c[0]} {c[1].name}" for c in self.within ])
        return f"[{self.name}: C:{s1} W:{s2}]"

def dump_bag_list(bag_list):
    for key, bag in bag_list.items():
        s1 = ', '.join([ f"{c[0]} {c[1].name}" for c in bag.contains ])
        s2 = ', '.join([ f"{c[0]} {c[1].name}" for c in bag.within ])
        print(f"{bag.name}:\n    Contains: {s1}\n    Within: {s2}")

def count_bags(bag_list, target):
    global outer_count

    bag = bag_list[target]
    count = 0

    for cont in bag.contains:
        count += cont[0]
        count += count_bags(bag_list, cont[1].name) * cont[0]

    return count

def main():
    bag_list = { }

    # Read in all the groups
    with open(fn, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break

            line = line.rstrip("\n")
            matches = re.findall(r'(.*) bags contain (.*)', line)

            cont_name = matches[0][0]
            content_list = matches[0][1].split(', ')
            cont_bag = bag_list.get(cont_name)
            if cont_bag == None:
                cont_bag = Bag(cont_name)
                bag_list[cont_name] = cont_bag

            for content in content_list:
                if content == 'no other bags.':
                    break
                matches = re.findall(r'(\d+) (.*) bag', content)
                count = matches[0][0]
                sub_name = matches[0][1]
                sub_bag = bag_list.get(sub_name)
                if sub_bag == None:
                    sub_bag = Bag(sub_name)
                    bag_list[sub_name] = sub_bag
                cont_bag.add_contains(count, sub_bag)
                sub_bag.add_within(count, cont_bag)

    count = count_bags(bag_list, 'shiny gold')
    return count

total = main()
print(f"Total count is {total}")
