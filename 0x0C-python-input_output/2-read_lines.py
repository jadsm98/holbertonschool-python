#!/usr/bin/python3
"""Module read n lines"""


def read_lines(filename="", nb_lines=0):
    """function read_lines"""

    with open(filename) as f:
        if nb_lines <= 0:
            for lines in f:
                print(lines, end="")
        else:
            for lines in f[nb_lines]:
                print(lines, end="")
