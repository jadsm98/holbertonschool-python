#!/usr/bin/python3
"""
Module
"""


def island_perimeter(grid):
    """
    Function to return the perimeter
    of an island
    """

    perim = 0
    for i, v in enumerate(grid):
        for j in range(len(v)):
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
