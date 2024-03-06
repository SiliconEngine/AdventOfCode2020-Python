#!/usr/bin/python
"""Advent of Code 2020, Day 22, Part 2

https://adventofcode.com/2020/day/22

Play a game of "Combat" using "Space Cards", which are just numbered
cards. Each round draws the top cards, compares the numbers, and the
winner has the highest card. The winner has their cards added to their deck.

In Part 2, if the hands are larger than the number on the drawn cards, then
a recursive game is played using a copy of the deck (otherwise, the rules are
as normal). The winner of that recursive game is the winner of the outer round.

See test.dat for sample data and hands.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'hands.dat'

import re
import queue
from collections import deque

# Cache to prevent loops
hand_cache = set()

# Duplicate a fifo queue of hands, limiting each one to the
# score of that sub-hand.
def dup_hands(player_hands, qty1, qty2):
    new1 = queue.Queue()
    new1.queue = deque(list(player_hands[0].queue)[:qty1])
    new2 = queue.Queue()
    new2.queue = deque(list(player_hands[1].queue)[:qty2])
    return [ new1, new2 ]

# Play the game, allowing recursive (nested) games
def play_game(player_hands):
    hand_cache = set()

    round = 0
    while True:
        round += 1
        tops = [player_hands[0].get(), player_hands[1].get()]

        # Check cache if this is a loop
        key = '-'.join(str(a) for a in list(player_hands[0].queue) + [ 'x' ] + list(player_hands[1].queue))
        if key in hand_cache:
            return 0                # Player 1 wins if hit the cache
        hand_cache.add(key)

        # If hand sizes are more than the card values, then we do a recursive game
        if player_hands[0].qsize() >= tops[0] and player_hands[1].qsize() >= tops[1]:
            winner = play_game(dup_hands(player_hands, tops[0], tops[1]))
        else:
            # Otherwise do a normal check of card values
            winner = 0 if tops[0] > tops[1] else 1

        # Round winner gets the two top cards
        player_hands[winner].put(tops[winner])
        player_hands[winner].put(tops[1-winner])

        # If queue is empty, then we can determine the game (or sub-game) winner
        if player_hands[1-winner].empty():
            break

    # Return game (or sub-game) winner
    return winner

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

    # Play top-level game
    winner = play_game(player_hands)

    # Calculate the score and return
    winning_list = list(player_hands[winner].queue)
    score = 0
    for idx in range(len(winning_list)):
        score += (idx+1) * winning_list[len(winning_list)-idx-1]

    return score

answer = main()
print(f"Answer is {answer}")
