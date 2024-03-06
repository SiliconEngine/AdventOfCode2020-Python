#!/usr/bin/python
"""Advent of Code 2020, Day 19, Part 2

https://adventofcode.com/2020/day/19

Given a list of nested string matching rules, figure out how
many strings match them. For part 2, two rules are replaced,
allowing for looped rules.

See test.dat for sample data and messages.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'messages.dat'

import re

class Rule:
    def __init__(self, rule_num, s):
        self.rule_num = rule_num
        self.or_list = [ ]
        self.constant = None

        if s[0] == '"':
            self.constant = s[1:-1]
            return

        set_list = s.split(' | ')
        for r in set_list:
            num_list = [ int(n) for n in r.split(' ') ]
            self.or_list.append(num_list)

    def __repr__(self):
        if self.constant != None:
            return f"[ {self.rule_num}: {self.constant} ]"

        if len(self.or_list) == 1:
            return f"[ {self.rule_num}: {self.or_list[0]} ]"
        else:
            return f"[ {self.rule_num}: {self.or_list[0]} | {self.or_list[1]} ]"

class RuleSet:
    def __init__(self):
        self.rules = { }

    # Add a Rule Object to rule set
    def add(self, rule_num, s):
        rule = Rule(rule_num, s)
        self.rules[rule_num] = rule

    # Recursive matching routine
    # Primary different with part 1 is allowing for multiple matches
    # to be returned.
    # Returns list of indexes of how far it made it on each path, or
    # an empty array if no match.
    def check_match(self, line, idx, rule_num):
        rule = self.rules[rule_num]

        # At absolute character?
        if rule.constant != None:
            if idx >= len(line):
                return []
            if line[idx] == rule.constant:
                return [ idx+1 ]
            return []

        good_list = []
        for num_list in rule.or_list:
            idx_list = [ idx ]
            for rule_num in num_list:
                new_list = [ ]
                for i in range(len(idx_list)):
                    new_idx = idx_list[i]
                    match_idxs = self.check_match(line, new_idx, rule_num)
                    new_list += match_idxs

                idx_list = new_list
                if len(idx_list) == 0:
                    break

            if len(idx_list) != 0:
                good_list += idx_list

        # Might be [] if no matches
        return good_list

    # Check if a string matches the pattern
    def has_match(self, line):
        # Start with rule 0
        new_idx_list = self.check_match(line, 0, 0)
        if len(new_idx_list) == 0:
            return False

        for new_idx in new_idx_list:
            if new_idx == len(line):
                return True

        return False

def main():
    rule_set = RuleSet()

    with open(fn, 'r') as file:
        # First read rules
        # Rule format:
        #     [rule num]: [rule num] [rule num]
        #     [rule num]: [rule num] [rule num] | [rule num] [rule num]
        #     [rule num]: "a"
        while True:
            line = file.readline()
            line = line.rstrip("\n")
            if line == '':
                break
            matches = re.findall(r'(\d+): (.*)', line)[0]
            rule_set.add(int(matches[0]), matches[1])

        # Read strings to match
        str_list = []
        while True:
            line = file.readline()
            if line == '':
                break
            line = line.rstrip("\n")
            str_list.append(line)

        # For part 2, these rules are replaced
        rule_set.add(8, '42 | 42 8')
        rule_set.add(11, '42 31 | 42 11 31')

        # Check strings against rules
        count = 0
        for line in str_list:
            if line in str_list:
                if rule_set.has_match(line):
                    count += 1

    return count

answer = main()
print(f"Answer is {answer}")
