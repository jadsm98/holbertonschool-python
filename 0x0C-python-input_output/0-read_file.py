#!/usr/bin/python3
"""Module to reads a file"""


def read_file(filename=""):
    """function that reads files"""

    with open(filename) as f:
        for line in f:
            print(line ,end="")
