#!/usr/bin/python
"""Advent of Code 2020, Day 16, Part 2

https://adventofcode.com/2020/day/16

Given a list of numbers on a list of train tickets, first eliminate
invalid tickets. Then determine which column of number corresponds
to the ticket number name based on the valid ranges and process of
elimination. Finally give product of "your ticket" numbers for the
numbers with names that start with "departure".

See test.dat for sample data and tickets.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test2.dat'
fn = 'tickets.dat'

import re

def main():
    rules = { }
    nearby_list = [ ]

    with open(fn, 'r') as file:
        # First is list of rules
        # [tag]: #-# or #-#
        while True:
            line = file.readline()
            line = line.rstrip("\n")
            if line == '':
                break
            matches = re.findall(r'([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)', line)[0]
            rules[matches[0]] = [ (int(matches[1]), int(matches[2])), (int(matches[3]), int(matches[4])) ]

        # "your ticket:"
        line = file.readline()

        # #,#,#
        my_ticket = [ int(n) for n in file.readline().rstrip("\n").split(',') ]
        line = file.readline()

        # "nearby tickets:"
        line = file.readline()

        while True:
            line = file.readline()
            if line == '':
                break
            ticket = [ int(n) for n in line.rstrip("\n").split(',') ]
            nearby_list.append(ticket)

    def check_valid(n):
        for rule in rules.values():
            if rule[0][0] <= n <= rule[0][1] or rule[1][0] <= n <= rule[1][1]:
                return True

        return False

    # Check for invalid numbers in the nearby_list and create list of valid tickets
    valid_tickets = []

    for ticket in nearby_list:
        invalid = False
        for n in ticket:
            if not check_valid(n):
                invalid = True
                break

        if not invalid:
            valid_tickets.append(ticket)

    # Create a list of lists of rule names, one row for each column of a ticket.
    # Then mark with '' where a ticket with a particular column violates a rule.
    rule_names = list(rules.keys())
    num_rules = len(rule_names)

    col_chk = []
    for idx in range(len(rule_names)):
        col_chk.append(rule_names.copy())

    for col_idx in range(num_rules):
        for ticket in valid_tickets:
            n = ticket[col_idx]
            for rule_idx in range(num_rules):
                rule_name = rule_names[rule_idx]
                rule = rules[rule_name]
                if not (rule[0][0] <= n <= rule[0][1] or rule[1][0] <= n <= rule[1][1]):
                    col_chk[col_idx][rule_idx] = ''

    # Last step, look for the row that only has one name left. Record that one,
    # and eliminate that name from the rest of the lists. Repeat until done.
    # Wrinkle: We end up with no possibilities, except one missing name, so we
    # know that's the last one.
    translate = { }
    debug = 0
    while len(list(translate)) < num_rules:
        found = False
        for col_idx in range(num_rules):
            count = 0
            for rule_idx in range(num_rules):
                if col_chk[col_idx][rule_idx] != '':
                    count += 1
                    found_name = col_chk[col_idx][rule_idx]
                    found_rule_idx = rule_idx
                    found_col_idx = col_idx
                    if count > 1:
                        break

            if count == 1:
                translate[found_name] = found_col_idx
                col_chk[found_col_idx] = [ '' ] * num_rules
                for col_idx in range(num_rules):
                    col_chk[col_idx][found_rule_idx] = ''
                found = True
                break

        if not found:
            # Check for exactly one left
            if num_rules - len(list(translate)) == 1:
                list1 = sorted(rule_names)
                list2 = sorted(translate.keys())
                list3 = [item for item in list1 if item not in list2]
                final_name = list3[0]

                list1 = list(range(0, num_rules))
                list2 = sorted(translate.values())
                list3 = [item for item in list1 if item not in list2]
                final_idx = list3[0]
                translate[final_name] = final_idx
                break

            # Shouldn't have any left over
            print(rule_names)
            print(translate)
            raise Exception('BAD')

    # Finally calculate the answer
    prod = 1
    for name in rule_names:
        if name[0:9] == 'departure':
            n = my_ticket[translate[name]]
            prod *= n

    return prod

answer = main()
print(f"Answer is {answer}")
