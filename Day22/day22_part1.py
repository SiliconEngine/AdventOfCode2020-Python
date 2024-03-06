#!/usr/bin/python
"""Advent of Code 2020, Day 22, Part 1

https://adventofcode.com/2020/day/22

Play a game of "Combat" using "Space Cards", which are just numbered
cards. Each round draws the top cards, compares the numbers, and the
winner has the highest card. The winner has their cards added to their
deck. The game loser runs out of cards and a score is determined.

See test.dat for sample data and hands.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'hands.dat'

import re
import queue

def main():
    player_hands = [ queue.Queue(), queue.Queue() ]
    with open(fn, 'r') as file:
        # Read in foods
        player = None
        while True:
            line = file.readline()
            if line == '':
                break
            line = line.rstrip('\n')

            if line[0:6] == 'Player':
                player = int(line[7])
                continue

            if line.isdigit():
                player_hands[player-1].put(int(line))

    round = 0
    while True:
        round += 1
        tops = [player_hands[0].get(), player_hands[1].get()]
        winner = 0 if tops[0] > tops[1] else 1
        player_hands[winner].put(tops[winner])
        player_hands[winner].put(tops[1-winner])

        if player_hands[1-winner].empty():
            break

    winning_list = list(player_hands[winner].queue)
    score = 0
    for idx in range(len(winning_list)):
        score += (idx+1) * winning_list[len(winning_list)-idx-1]

    return score

answer = main()
print(f"Answer is {answer}")
