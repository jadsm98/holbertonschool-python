#!/usr/bin/python3
"""
Module
"""


def island_perimeter(grid):
    """
    Function to return the perimeter
    of an island
    """
    if len(grid) > 100 or any(len(i) for i in grid) > 100:
        return

    perim = 0
    for i, v in enumerate(grid):
        for j in range(len(v)):
            if grid[0][j] != 0 or grid[i][0] != 0 \
               or grid[-1][j] != 0 or grid[i][-1] != 0:
                return
            if grid[i][j] == 1:
                if grid[i - 1][j] == 0:
                    perim += 1
                if grid[i + 1][j] == 0:
                    perim += 1
                if grid[i][j - 1] == 0:
                    perim += 1
                if grid[i][j + 1] == 0:
                    perim += 1
    return perim
