#!/usr/bin/python
"""Advent of Code 2020, Day 17, Part 1

https://adventofcode.com/2020/day/17

Give a map of cubes, apply a set of rules that change a flag on each cube
that is active or inactive. Count number of active cubes at end of six
cycles.

See test.dat for sample data and tickets.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'cube_map.dat'

import re

def make_key(x, y, z):
    return f"{x},{y},{z}"

class Cube:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.active = False
        self.new_active = None

    def get_key(self):
        return make_key(self.x, self.y, self.z)

    def __repr__(self):
        return f"[{self.x},{self.y},{self.z}: {self.active}]"


class CubeSet:
    def __init__(self):
        self.cubes = { }
        self.x_range = [0, 0]
        self.y_range = [0, 0]
        self.z_range = [0, 0]

    def update_range(self, cube):
        x, y, z = cube.x, cube.y, cube.z

        if len(self.cubes) == 0:
            self.x_range = [ x, x ]
            self.y_range = [ y, y ]
            self.z_range = [ z, z ]
        else:
            if x < self.x_range[0]:
                self.x_range[0] = x
            if x > self.x_range[0]:
                self.x_range[1] = x
            if y < self.y_range[0]:
                self.y_range[0] = y
            if y > self.y_range[0]:
                self.y_range[1] = y
            if z < self.z_range[0]:
                self.z_range[0] = z
            if z > self.z_range[0]:
                self.z_range[1] = z

    # Add a cube to cube set
    def add(self, cube):
        key = cube.get_key()
        self.cubes[key] = cube
        self.update_range(cube)

    # Get a cube from set, creating it if it doesn't exist
    def get(self, x, y, z):
        key = make_key(x, y, z)
        cube = self.cubes.get(key)
        if cube == None:
            cube = Cube(x, y, z)
            self.add(cube)

        return cube

    # Apply rules to a cube, setting new_active
    def apply_cube(self, x, y, z):
        cube = self.get(x, y, z)

        # Count how many active neighbors
        active_count = 0
        for x in range(cube.x-1, cube.x+2):
            for y in range(cube.y-1, cube.y+2):
                for z in range(cube.z-1, cube.z+2):
                    if x == cube.x and y == cube.y and z == cube.z:
                        continue            # Skip self
                    neighbor = self.get(x, y, z)
                    if neighbor.active:
                        active_count += 1

        cube.new_active = None
        if cube.active and active_count not in (2, 3):
            cube.new_active = False

        if not cube.active and active_count == 3:
            cube.new_active = True

        return

    # Apply rules to all cubes
    def apply_cycle(self):
        x_range = self.x_range.copy()
        y_range = self.y_range.copy()
        z_range = self.z_range.copy()
        for x in range(x_range[0]-1, x_range[1]+2):
            for y in range(y_range[0]-1, y_range[1]+2):
                for z in range(z_range[0]-1, z_range[1]+2):
                    self.apply_cube(x, y, z)

        for cube in self.cubes.values():
            if cube.new_active != None:
                cube.active = cube.new_active

    # Count number of cubes in active state
    def count_active(self):
        count = 0
        for cube in self.cubes.values():
            if cube.active == True:
                count += 1

        return count

def main():
    cube_set = CubeSet()

    with open(fn, 'r') as file:
        y, z = 0, 0
        for line in file:
            line = line.rstrip("\n")
            x = 0
            for c in line:
                cube = Cube(x, y, z)
                cube_set.add(cube)
                if c == '#':
                    cube.active = True
                x += 1
            y += 1

    for cycle in range(6):
        cube_set.apply_cycle()

    return 0

answer = main()
print(f"Answer is {answer}")
