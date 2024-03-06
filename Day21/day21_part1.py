#!/usr/bin/python
"""Advent of Code 2020, Day 21, Part 1

https://adventofcode.com/2020/day/21

Given a list of ingredients (in a foreign language) and what allergens might
be contained, figure out how many ingredients are not allergens based
on process of elimination.

See test.dat for sample data and foods.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'foods.dat'

import re
from collections import defaultdict

def main():
    # This dictionary maps each allergen to a list of sets of possible ingredients.
    allergen_map = defaultdict(list)

    # This dictionary keeps track of how many times each ingredient appears across all foods.
    ingredient_appearances = defaultdict(int)

    with open(fn, 'r') as file:
        # Read in foods
        while True:
            line = file.readline()
            if line == '':
                break

            matches = re.findall(r'(.*) \(contains (.*)\)', line)[0]
            #foods.append((matches[0], matches[1])

            # Split the string of ingredients into a set of individual ingredients.
            ingredients = set(matches[0].split())

            # Update the count of appearances for each ingredient.
            for ingredient in ingredients:
                ingredient_appearances[ingredient] += 1

            # For each allergen listed with the food, update its possible ingredients.
            for allergen in matches[1].split(', '):
                if allergen in allergen_map:
                    # If the allergen has been seen before, intersect its current possible ingredients
                    # with the new set of possible ingredients (i.e., ingredients of the current food).
                    allergen_map[allergen].append(ingredients)
                else:
                    # If this is the first time the allergen is seen, initialize its possible ingredients.
                    allergen_map[allergen] = [ingredients]

    # Intersect ingredient lists for each allergen to narrow down possibilities.
    for allergen in allergen_map:
        # Use set intersection to find common ingredients among all lists of possible ingredients
        # for this allergen.
        possible_ingredients = set.intersection(*allergen_map[allergen])
        allergen_map[allergen] = possible_ingredients

    # Initialize a dictionary to hold confirmed allergen-ingredient pairs.
    confirmed_allergens = {}

    # Keep solving for confirmed allergen-ingredient mappings until all are found.
    while len(confirmed_allergens) < len(allergen_map):
        for allergen, ingredients in allergen_map.items():
            # Remove any ingredients that have already been confirmed to contain other allergens.
            ingredients -= set(confirmed_allergens.values())
            # If only one ingredient remains, it must be the carrier of the current allergen.
            if len(ingredients) == 1:
                confirmed_ingredient = ingredients.pop()
                confirmed_allergens[allergen] = confirmed_ingredient
                break  # Exit the loop early to re-start the while loop since we made a confirmation.

    # Identify safe ingredients by subtracting the set of confirmed allergen-containing ingredients
    # from the set of all ingredients.
    safe_ingredients = set(ingredient_appearances) - set(confirmed_allergens.values())

    # Count the total appearances of safe ingredients in all foods.
    safe_ingredient_count = sum(ingredient_appearances[ingredient] for ingredient in safe_ingredients)

    # The final result is the total number of appearances of safe ingredients.
    return safe_ingredient_count

answer = main()
print(f"Answer is {answer}")
