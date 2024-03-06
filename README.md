# Advent of Code 2020 solutions written in Python.
## Author: Tim Behrendsen

Link: https://adventofcode.com/2020/

Advent of Code is a series of puzzles over 25 days, each with a part 1 and
part 2. The difficulty roughly rises each day, with the later puzzles often
requiring some tricky algorithms to solve.

For these solutions, the various days are in separate directories, with a
separate file for each part. Day 25, as traditional, is only a single part.

### Advent of Code 2020, Day 1, Part 1

Link: https://adventofcode.com/2020/day/1

Given a list of numbers, find the two that total to 2020.

### Advent of Code 2020, Day 1, Part 2

Link: https://adventofcode.com/2020/day/1

Given a list of number, find the three that total to 2020.

### Advent of Code 2020, Day 2, Part 1

Link: https://adventofcode.com/2020/day/2

Parse a "password rule" policy and determine if each line is correct.
Display how many pass the rule.

### Advent of Code 2020, Day 2, Part 2

Link: https://adventofcode.com/2020/day/2

Parse a "password rule" policy and determine if each line is correct.
Display how many pass the rule. Slightly more complicated rule in Part 2.

### Advent of Code 2020, Day 3, Part 1 and Part 2

Link: https://adventofcode.com/2020/day/3

Input: a map of a slope and trees.<br>
Part 1: How many trees are encountered traversing right 3 and down 1.<br>
Part 2: Similar, but use five different slope numbers.

### Advent of Code 2020, Day 4, Part 1

Link: https://adventofcode.com/2020/day/4

Given a list of passport fields, determine how many have all required
fields.

### Advent of Code 2020, Day 4, Part 2

Link: https://adventofcode.com/2020/day/4

Given a list of field validation rules for a list of passports, determine
number of valid ones.

### Advent of Code 2020, Day 5, Part 1

Link: https://adventofcode.com/2020/day/5

An airline uses a "binary space partition" seating arrangement, where you
get "F"(front) or "B"(back) letters to divide the seating rows, then
"L" or "R" to divide the row to determine the seat. Convert the letters
to seat numbers and identify the highest seat.

### Advent of Code 2020, Day 5, Part 2

Link: https://adventofcode.com/2020/day/5

An airline uses a "binary space partition" seating arrangement, where you
get "F"(front) or "B"(back) letters to divide the seating rows, then
"L" or "R" to divide the row to determine the seat. Convert the letters
to seat numbers. Identify a seat missing from the list, with the caveat
that seats at the front and back are missing, so the one we want is in
the middle.

### Advent of Code 2020, Day 6, Part 1

Link: https://adventofcode.com/2020/day/6

Given a list of group answers, count the number of questions to which
anyone answered "yes", and sum them up.

### Advent of Code 2020, Day 6, Part 2

Link: https://adventofcode.com/2020/day/6

Given a list of group answers, count the number of questions to which
everyone answered "yes", and sum them up.

### Advent of Code 2020, Day 7, Part 1

Link: https://adventofcode.com/2020/day/7

Given a set of rules about how many specific colored bags can be
contained within a different bag, figure out how many bag colors
can contain one shiny gold bag, with nesting allowed.

### Advent of Code 2020, Day 7, Part 2

Link: https://adventofcode.com/2020/day/7

Given a set of rules about how many specific colored bags can be
contained within a different bag, figure out how many bags can be
contained within one shiny gold bag, with nesting allowed.

### Advent of Code 2020, Day 8, Part 1

Link: https://adventofcode.com/2020/day/8

Given a list of program instructions (nop, jmp and acc), follow the
instructions and terminate when the same instruction is executed twice.
Show the final accumulator value.

### Advent of Code 2020, Day 8, Part 2

Link: https://adventofcode.com/2020/day/8

Given a list of program instructions (nop, jmp and acc), follow the
instructions, but there is one instruction that has to either be changed
from a jmp->nop, or a nop->jmp, in order to execute the last instruction.
Otherwise, will go into a loop.

### Advent of Code 2020, Day 9, Part 1

Link: https://adventofcode.com/2020/day/9

Give a list of numbers, identify which number is not a sum of two of the prior
numbers in a certain window size (5 in the test, 25 in the full data set).

### Advent of Code 2020, Day 9, Part 2

Link: https://adventofcode.com/2020/day/9

Give a list of numbers, find a contiguous series in the list that add
up to a target number.

### Advent of Code 2020, Day 10, Part 1

Link: https://adventofcode.com/2020/day/10

Given a list of "joltages" for a group of adapters, determine the number
of 1 jolt differences and 3 jolt differences.

### Advent of Code 2020, Day 10, Part 2

Link: https://adventofcode.com/2020/day/10

Give a list of "joltages" for a group of adapters, determine the number
of combinations of adapters that convert 0 jolts to the final number.
An adapter can increase the joltages only a maximum of three.

Recursive algorithm that uses dynamic programming to solve the problem
quickly by caching intermediate results.

### Advent of Code 2020, Day 11, Part 1

Link: https://adventofcode.com/2020/day/11

Given a map of seats, apply rules of people being seated / unseated.
Continue until the map no longer changes. Rules check adjacent seats.

### Advent of Code 2020, Day 11, Part 2

Link: https://adventofcode.com/2020/day/11

Given a map of seats, apply rules of people being seated / unseated.
Continue until the map no longer changes. For part 2, need to scan
along rows/columns to determine the rule.

### Advent of Code 2020, Day 12, Part 1

Link: https://adventofcode.com/2020/day/12

Given a set of ship movement instructions, determine the final
position of the ship.

### Advent of Code 2020, Day 12, Part 2

Link: https://adventofcode.com/2020/day/12

Given a set of movement instructions, some for a ship's position, and some
for a "waypoint", determine the ship's final position as it follows the
waypoint.

### Advent of Code 2020, Day 13, Part 1

Link: https://adventofcode.com/2020/day/13

Given a list of buses and the cycle intervals they depart, calculate the earliest
bus and the number of minutes needed to wait.

### Advent of Code 2020, Day 13, Part 2

Link: https://adventofcode.com/2020/day/13

Given a list of buses and the cycle intervals they depart, calculate the
earliest time where they would each depart at the offsets matching their
positions in the list.

This is tricky to do with closed-form math, but an algorithm that tracks
the repeating cycle when adding each bus, and then looping through the
cycles when adding a new bus until it fits the pattern gives an efficient
solution.

### Advent of Code 2020, Day 14, Part 1

Link: https://adventofcode.com/2020/day/14

Given input data that has a mask, along with setting memory locations,
assign each memory location after applying the mask to the number.
Add up all the numbers.

### Advent of Code 2020, Day 14, Part 2

Link: https://adventofcode.com/2020/day/14

Given input data of a mask and setting memory locations, apply the mask
to the memory location before assignment. The wrinkle is that if there is
an 'X' in the mask, then that counts as either a 0 or a 1, and both memory
locations are assigned. Once all assigned, add up all the numbers.

The number of potential memory locations was small enough that just
unpacking all the addresses work reasonably.

### Advent of Code 2020, Day 15, Part 1

Link: https://adventofcode.com/2020/day/15

Simulate elf memory game, doing 2020 rounds.

### Advent of Code 2020, Day 15, Part 2

Link: https://adventofcode.com/2020/day/15

Simulate elf memory game, doing 30,000,000 rounds.

### Advent of Code 2020, Day 16, Part 1

Link: https://adventofcode.com/2020/day/16

Given a list of numbers on a list of train tickets, determine which
ticket numbers are valid based on range rules. Return sum of invalid
numbers.

### Advent of Code 2020, Day 16, Part 2

Link: https://adventofcode.com/2020/day/16

Given a list of numbers on a list of train tickets, first eliminate
invalid tickets. Then determine which column of number corresponds
to the ticket number name based on the valid ranges and process of
elimination. Finally give product of "your ticket" numbers for the
numbers with names that start with "departure".

### Advent of Code 2020, Day 17, Part 1

Link: https://adventofcode.com/2020/day/17

Give a map of cubes, apply a set of rules that change a flag on each cube
that is active or inactive. Count number of active cubes at end of six
cycles.

### Advent of Code 2020, Day 17, Part 2

Link: https://adventofcode.com/2020/day/17

Give a map of 4D hypercubes, apply a set of rules that change a flag on each
cube that is active or inactive. Count number of active hypercubes at end of six
cycles.

### Advent of Code 2020, Day 18, Part 1

Link: https://adventofcode.com/2020/day/18

Simple expression evaluator that doesn't use precedence.

### Advent of Code 2020, Day 18, Part 2

Link: https://adventofcode.com/2020/day/18

Expression evaluator that uses opposite precedence from the norm, where '+'
has higher precedence than '*'. Uses two-stack algorithm for eval.

### Advent of Code 2020, Day 19, Part 1

Link: https://adventofcode.com/2020/day/19

Given a list of nested string matching rules, figure out how
many strings match them.

### Advent of Code 2020, Day 19, Part 2

Link: https://adventofcode.com/2020/day/19

Given a list of nested string matching rules, figure out how
many strings match them. For part 2, two rules are replaced,
allowing for looped rules.

### Advent of Code 2020, Day 20, Part 1

Link: https://adventofcode.com/2020/day/20

Given a set of tiles with 10x10 matrix of '.' and '#', identify
how they can be assembled into an interlocking grid with common
edges. The tiles can be rotated or flipped along an axis to fit.
The puzzle answer is the product of the tile numbers of the four
corners.

Since we just need to identify the corners, this program builds
a hash of each edge backward and forward, then figures out which
four tiles only have two edges in common with other tiles.

### Advent of Code 2020, Day 20, Part 2

Link: https://adventofcode.com/2020/day/20

Given a set of tiles with 10x10 matrix of '.' and '#', identify
how they can be assembled into an interlocking grid with common
edges. The tiles can be rotated or flipped along an axis to fit.
Once the grid is assembled, find the number of "serpents" that match
the serpent pattern. Calculate the number of non-serpent hash marks

This builds a list of all the tiles in each possible orientation, then
finds all the common edges. The data is "friendly" in that there aren't
any ambiguous edges, so once you build the list of common edges, it's
fairly straight forward to start at a corner and move to the next
adjoining tile.

### Advent of Code 2020, Day 21, Part 1

Link: https://adventofcode.com/2020/day/21

Given a list of ingredients (in a foreign language) and what allergens might
be contained, figure out how many ingredients are not allergens based
on process of elimination.

### Advent of Code 2020, Day 21, Part 2

Link: https://adventofcode.com/2020/day/21

Given a list of ingredients (in a foreign language) and what allergens might
be contained, figure out which ingredients are allergens based on process of
elimination.

### Advent of Code 2020, Day 22, Part 1

Link: https://adventofcode.com/2020/day/22

Play a game of "Combat" using "Space Cards", which are just numbered
cards. Each round draws the top cards, compares the numbers, and the
winner has the highest card. The winner has their cards added to their
deck. The game loser runs out of cards and a score is determined.

### Advent of Code 2020, Day 22, Part 2

Link: https://adventofcode.com/2020/day/22

Play a game of "Combat" using "Space Cards", which are just numbered
cards. Each round draws the top cards, compares the numbers, and the
winner has the highest card. The winner has their cards added to their deck.

In Part 2, if the hands are larger than the number on the drawn cards, then
a recursive game is played using a copy of the deck (otherwise, the rules are
as normal). The winner of that recursive game is the winner of the outer round.

### Advent of Code 2020, Day 23, Part 1

Link: https://adventofcode.com/2020/day/23

Given a set up of nine cups in a circle labeled 1-9, move them according
to a set of rules and after 100 iterations, determine the final layout.

### Advent of Code 2020, Day 23, Part 2

Link: https://adventofcode.com/2020/day/23

Given a set up of nine cups in a circle labeled 1-9, along with more cups
from 10 through 1,000,000, move them according to a set of rules and
determine the final layout, but we're doing 10,000,000 moves.

Requires an efficient data structure, but overall needed to be brute force.

### Advent of Code 2020, Day 24, Part 1

Link: https://adventofcode.com/2020/day/24

For a grid of hexagonal tiles, follow a path of directions and flip the
color of the tile at the end between white to black. Figure out the number
of black tiles at the end.

Flat side is East-West. Uses a coordinate system like:

```
[0,0]  [2,0]  [4,0]
   [1,0]  [3,0]  [5,0]
[0,1]  [2,1]  [4,1]
   [1,1]  [3,1]  [5,1]
```

### Advent of Code 2020, Day 24, Part 2

Link: https://adventofcode.com/2020/day/24

For a grid of hexagonal tiles, follow a path of directions and flip the
color of the tile at the end between white to black. Then perform rules
of flipping tiles based on the number of adjacent black tiles. Figure out
the final number of black tiles at the end.

Flat side is East-West. Uses a coordinate system like:

```
[0,0]  [2,0]  [4,0]
   [1,0]  [3,0]  [5,0]
[0,1]  [2,1]  [4,1]
   [1,1]  [3,1]  [5,1]
```

### Advent of Code 2020, Day 24, Part 1

Link: https://adventofcode.com/2020/day/24

Given a set of "public keys", determine the private key using the supplied
algorithm. This is pretty much just an easy brute-force problem.

