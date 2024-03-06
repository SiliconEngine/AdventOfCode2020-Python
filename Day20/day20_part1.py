#!/usr/bin/python
"""Advent of Code 2020, Day 20, Part 1

https://adventofcode.com/2020/day/20

Given a set of tiles with 10x10 matrix of '.' and '#', identify
how they can be assembled into an interlocking grid with common
edges. The tiles can be rotated or flipped along an axis to fit.
The puzzle answer is the product of the tile numbers of the four
corners.

Since we just need to identify the corners, this program builds
a hash of each edge backward and forward, then figures out which
four tiles only have two edges in common with other tiles.

See test.dat for sample data and tiles.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'tiles.dat'

import re
from functools import reduce

class Tile:
    def __init__(self, tile_num, row_list):
        self.tile_num = tile_num
        self.row_list = row_list

        # Generate all edge combinations, rotated and flipped
        edge_list = { }
        edge_list['top'] = row_list[0]
        edge_list['top-rev'] = row_list[0][::-1]
        edge_list['bot'] = row_list[-1]
        edge_list['bot-rev'] = row_list[-1][::-1]

        side = self.get_col(0)
        edge_list['lft'] = side
        edge_list['lft-rev'] = side[::-1]

        side = self.get_col(9)
        edge_list['rgt'] = side
        edge_list['rgt-rev'] = side[::-1]
        self.edge_list = edge_list

    # Return column characters of tiles as a string
    def get_col(self, col):
        clist = []
        for i in range(len(self.row_list)):
            clist.append(self.row_list[i][col])
        return ''.join(clist)

class TileSet:
    def __init__(self):
        self.tiles = []
        self.edge_hash = { }

    # Add a tile to the set of tiles
    def add(self, tile):
        self.tiles.append(tile)
        # Add tile edges to the edge hash
        for key, edge in tile.edge_list.items():
            if self.edge_hash.get(edge) == None:
                self.edge_hash[edge] = [ ]
            self.edge_hash[edge].append([ tile, key ])

    # Identify the four corners of the tiles
    def find_corners(self):
        tile_edges = { }
        for key, edge_list in self.edge_hash.items():
            if len(edge_list) > 1:
                for edge in edge_list:
                    tile_edges.setdefault(edge[0].tile_num, [])
                    tile_edges[edge[0].tile_num].append(edge[1])

        # Identify corners, which should only have edges that match other tiles
        # on perpendicular sides
        corner_list = []
        for tile_num, edge_list in tile_edges.items():
            edge_set = set([ name[0:3] for name in edge_list ])
            if len(edge_set) == 2:
                if 'rgt' in edge_set and ('bot' in edge_set or 'top' in edge_set):
                    corner_list.append(tile_num)
                elif 'lft' in edge_set and ('bot' in edge_set or 'top' in edge_set):
                    corner_list.append(tile_num)

        return corner_list

def main():
    tile_set = TileSet()

    with open(fn, 'r') as file:
        # Read in tiles
        while True:
            line = file.readline()
            if line == '':
                break

            matches = re.findall(r'Tile (\d+)', line)
            tile_num = int(matches[0])
            new_tile = []
            for i in range(10):
                line = file.readline()
                line = line.rstrip("\n")
                new_tile.append(line)

            tile = Tile(tile_num, new_tile)
            tile_set.add(tile)

            # Skip blank line
            line = file.readline()

    corner_list = tile_set.find_corners()

    return reduce(lambda x, y: x*y, corner_list)

answer = main()
print(f"Answer is {answer}")
