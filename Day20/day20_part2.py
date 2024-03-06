#count!/usr/bin/python
"""Advent of Code 2020, Day 20, Part 2

https://adventofcode.com/2020/day/20

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

See test.dat for sample data and tiles.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'tiles.dat'

total_tiles = 0

import re

# Rotate characters of a list strings 90 deg right
def rotate_right(row_list):
    return ["".join(row) for row in zip(*row_list[::-1])]

# Invert columns of a list of strings
def invert_cols(row_list):
    return [ row[::-1] for row in row_list ]

# Invert rows of a list of strings
def invert_rows(row_list):
    return row_list[::-1]

# Count the number of serpents in the grid
def count_serpents(grid):
    # Serpent. Note the dots are "match any", not literal dots.
    serp1 = '..................#.'
    serp2 = '#....##....##....###'
    serp3 = '.#..#..#..#..#..#...'

    count = 0
    for rowidx in range(1, len(grid)-1):
        line2 = grid[rowidx]

        # Get indexes of the middle pattern matches
        # For each one, see if the outer patterns match at same place.
        idxs = [match.start() for match in re.finditer(serp2, line2)]
        for idx in idxs:
            line1 = grid[rowidx-1]
            if not re.search(serp1, line1[idx:idx+20]):
                continue
            line3 = grid[rowidx+1]
            if not re.search(serp3, line3[idx:idx+20]):
                continue

            count += 1

    return count

class Tile:
    def __init__(self, tile_num, row_list, tag):
        self.tile_num = f"{tile_num}/{tag}"
        self.row_list = row_list
        self.tag = tag

        # Generate all edge combinations, rotated and flipped
        edge_list = { }
        edge_list['top'] = row_list[0]
        edge_list['bot'] = row_list[-1]

        side = self.get_col(0)
        edge_list['lft'] = side

        side = self.get_col(9)
        edge_list['rgt'] = side
        self.edge_list = edge_list

    def __repr__(self):
        return f"[Tile {self.tile_num}]"

    # Return column characters of tiles as a string
    def get_col(self, col):
        clist = []
        for i in range(len(self.row_list)):
            clist.append(self.row_list[i][col])
        return ''.join(clist)

class TileSet:
    def __init__(self):
        self.tiles = {}
        self.edge_hash = { }
        self.tile_hash = { }

    # Add a tile to the set of tiles
    def add(self, tile):
        self.tiles[tile.tile_num] = tile

        # Add tile edges to the edge hash
        for key, edge in tile.edge_list.items():
            if self.edge_hash.get(edge) == None:
                self.edge_hash[edge] = [ ]
            self.edge_hash[edge].append([ tile, key ])

    # Find all the edges that tiles have in common
    def find_common_edges(self):
        # hash of edge patterns
        tile_edges = { }

        for key, edge_list in self.edge_hash.items():
            for edge in edge_list:
                tile = edge[0]
                side = edge[1]
                for edge2 in edge_list:
                    tile2 = edge2[0]
                    if tile2.tile_num[0:4] == tile.tile_num[0:4]:     # Don't match with self
                        continue
                    side2 = edge2[1]

                    # Two sides have matching patterns, but are they along
                    # the same orientation?
                    if (side == 'lft' and side2 != 'rgt') or \
                            (side == 'rgt' and side2 != 'lft') or \
                            (side == 'top' and side2 != 'bot') or \
                            (side == 'bot' and side2 != 'top'):
                        continue

                    # Yes, store away
                    k = f"{tile.tile_num}"
                    tile_edges.setdefault(k, {})
                    tile_edges[k].setdefault(side, [])
                    tile_edges[k][side].append([ tile2, side2, key])

        self.tile_edges = tile_edges

    # Identify the four corners of the tiles
    def find_corners(self):
        # Identify corners, which should only have edges that match other tiles
        # on perpendicular sides
        corner_list = []
        for tile_num, edge_list in self.tile_edges.items():
            edge_set = set([ side for side, edge in edge_list.items() ])
            if len(edge_set) == 2:
                if 'rgt' in edge_set and ('bot' in edge_set or 'top' in edge_set):
                    corner_list.append(tile_num)
                elif 'lft' in edge_set and ('bot' in edge_set or 'top' in edge_set):
                    corner_list.append(tile_num)

        return corner_list

    # Given a corner, traverse through common edges, building up the puzzle.
    # There could possibly be many solutions, depending on what corner you
    # start on and what orientation.
    # Returns 'none' if an adjoining edge isn't found, which means the
    # starting corner didn't have a solution.
    def build_matrix(self, corner_nums, first_corner):
        tile_rows = [ ]
        tile_cols = [ first_corner ]
        cur_tile_num = tile_cols[0]
        tile_count = 1
        total_cols = None
        while True:
            tile_edges = self.tile_edges[cur_tile_num]

            # Move to next tile on the right
            next_tile_data = tile_edges.get('rgt')
            if next_tile_data == None:
                return None
            if len(next_tile_data) != 1:
                raise Exception("MULTIPLE TILES")

            next_tile_num = next_tile_data[0][0].tile_num
            tile_cols.append(next_tile_num)
            tile_count += 1

            # See if hit end of building the row
            if (total_cols != None and len(tile_cols) == total_cols) or \
                    (total_cols == None and next_tile_num[0:4] in corner_nums):
                tile_rows.append(tile_cols)

                # See if this is the final tile
                total_cols = len(tile_cols)
                if tile_count == total_tiles:
                    break

                # Move to tile below first tile
                first_tile_num = tile_cols[0]
                tile_cols = [ ]
                tile_edges = self.tile_edges[first_tile_num]
                next_tile_data = tile_edges.get('bot')
                if next_tile_data == None:
                    return None
                if len(next_tile_data) != 1:
                    raise Exception("MULTIPLE TILES")

                next_tile_num = next_tile_data[0][0].tile_num
                tile_cols.append(next_tile_num)
                tile_count += 1

            cur_tile_num = next_tile_num

        return tile_rows

    # Given the matrix of tiles, return a list of strings of assembled tiles.
    # For assembly, the top, bottom, left and right edges are removed.
    def gen_grid(self, matrix):
        str_list = []
        for tile_row in matrix:
            for s_row in range(1, 9):
                s = []
                for tile_col in tile_row:
                    tile = self.tiles[tile_col]
                    s.append(tile.row_list[s_row][1:9])

                str_list.append(''.join(s))

        return str_list

def main():
    global total_tiles
    tile_set = TileSet()

    total_tiles = 0
    with open(fn, 'r') as file:
        # Read in tiles
        while True:
            line = file.readline()
            if line == '':
                break

            total_tiles += 1
            matches = re.findall(r'Tile (\d+)', line)
            tile_num = int(matches[0])
            new_tile = []
            for i in range(10):
                line = file.readline()
                line = line.rstrip("\n")
                new_tile.append(line)

            # For each tile, we produce all the combinations of rotations/inversions.
            # Note that invert_rows() wasn't necessary, because it was redundant
            # with a rotation + invert_cols().
            temp_tile = new_tile.copy()
            chk_list = []
            for r in range(4):
                tile = Tile(tile_num, temp_tile, f"r{r}---")
                chk_list.append([ f"r{r}---", temp_tile.copy() ])
                tile_set.add(tile)

                inv_col = invert_cols(temp_tile)
                tile = Tile(tile_num, inv_col, f"r{r}-ic")
                chk_list.append([ f"r{r}-ic", inv_col.copy() ])
                tile_set.add(tile)

                temp_tile = rotate_right(temp_tile)

            # Skip blank line
            line = file.readline()

    # Build list of common edges between tiles
    tile_set.find_common_edges()

    # Locate corners of tile set
    corner_nums = set()
    corner_list = tile_set.find_corners()
    for corner in sorted(corner_list):
        corner_nums.add(corner[0:4])

    # Pick a corner, and find all adjacent tiles
    good_list = []
    for first_corner in corner_list:
        tile_rows = tile_set.build_matrix(corner_nums, first_corner)
        if tile_rows != None:
            good_list.append([ first_corner, tile_rows ])

    # Count the number '#' hash characters in grid
    def total_hashes(grid):
        hash_count = 0
        for row in grid:
            for col in row:
                if col == '#':
                    hash_count += 1
        return hash_count

    # Check each matrix. One of the combinations is the one where
    # we can identify the serpants, so we just do them all until
    # we find the most serpents (and thus the fewest non-serpent
    # hash characters)
    #
    # Note each serpent takes up 15 hashes, so we can just subtract
    # from the total number.
    min_answer = 9999
    for corner, matrix in good_list:
        grid = tile_set.gen_grid(matrix)
        count = count_serpents(grid)

        answer = total_hashes(grid) - 15 * count
        min_answer = min(min_answer, answer)

    return min_answer

answer = main()
print(f"Answer is {answer}")
