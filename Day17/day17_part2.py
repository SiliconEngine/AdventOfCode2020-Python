#!/usr/bin/python
"""Advent of Code 2020, Day 17, Part 2

https://adventofcode.com/2020/day/17

Give a map of 4D hypercubes, apply a set of rules that change a flag on each
cube that is active or inactive. Count number of active hypercubes at end of six
cycles.

See test.dat for sample data and tickets.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'cube_map.dat'

import re

def make_key(x, y, z, w):
    return f"{x},{y},{z},{w}"

class Cube:
    def __init__(self, x, y, z, w):
        self.x, self.y, self.z, self.w = x, y, z, w
        self.active = False
        self.new_active = None

    def get_key(self):
        return make_key(self.x, self.y, self.z, self.w)

    def __repr__(self):
        return f"[{self.x},{self.y},{self.z},{self.w}: {self.active}]"


class CubeSet:
    def __init__(self):
        self.cubes = { }
        self.x_range = [0, 0]
        self.y_range = [0, 0]
        self.z_range = [0, 0]
        self.w_range = [0, 0]

    def update_range(self, cube):
        x, y, z, w = cube.x, cube.y, cube.z, cube.w

        if len(self.cubes) == 0:
            self.x_range = [ x, x ]
            self.y_range = [ y, y ]
            self.z_range = [ z, z ]
            self.w_range = [ w, w ]
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
            if w < self.w_range[0]:
                self.w_range[0] = w
            if w > self.w_range[0]:
                self.w_range[1] = w

    # Add a cube to cube set
    def add(self, cube):
        key = cube.get_key()
        self.cubes[key] = cube
        self.update_range(cube)

    # Get a cube from data structure and create it if it doesn't exist.
    def get(self, x, y, z, w):
        key = make_key(x, y, z, w)
        cube = self.cubes.get(key)
        if cube == None:
            cube = Cube(x, y, z, w)
            self.add(cube)

        return cube

    # Apply rules to a single cube and set new_active to new state
    def apply_cube(self, x, y, z, w):
        cube = self.get(x, y, z, w)

        # Count how many active neighbors
        active_count = 0
        for x in range(cube.x-1, cube.x+2):
            for y in range(cube.y-1, cube.y+2):
                for z in range(cube.z-1, cube.z+2):
                    for w in range(cube.w-1, cube.w+2):
                        if x == cube.x and y == cube.y and z == cube.z and w == cube.w:
                            continue            # Skip self
                        neighbor = self.get(x, y, z, w)
                        if neighbor.active:
                            active_count += 1

        cube.new_active = None
        if cube.active and active_count not in (2, 3):
            cube.new_active = False

        if not cube.active and active_count == 3:
            cube.new_active = True

        return

    # Apply rules to our list of cubes
    def apply_cycle(self):
        x_range = self.x_range.copy()
        y_range = self.y_range.copy()
        z_range = self.z_range.copy()
        w_range = self.w_range.copy()
        for x in range(x_range[0]-1, x_range[1]+2):
            for y in range(y_range[0]-1, y_range[1]+2):
                for z in range(z_range[0]-1, z_range[1]+2):
                    for w in range(w_range[0]-1, w_range[1]+2):
                        self.apply_cube(x, y, z, w)

        for cube in self.cubes.values():
            if cube.new_active != None:
                cube.active = cube.new_active

    def count_active(self):
        count = 0
        for cube in self.cubes.values():
            if cube.active == True:
                count += 1

        return count

def main():
    cube_set = CubeSet()

    with open(fn, 'r') as file:
        y, z, w = 0, 0, 0
        for line in file:
            line = line.rstrip("\n")
            x = 0
            for c in line:
                cube = Cube(x, y, z, w)
                cube_set.add(cube)
                if c == '#':
                    cube.active = True
                x += 1
            y += 1

    for cycle in range(6):
        cube_set.apply_cycle()
        print(f"Cycle {cycle+1}: num active = {cube_set.count_active()}")

    return 0

answer = main()
print(f"Answer is {answer}")
