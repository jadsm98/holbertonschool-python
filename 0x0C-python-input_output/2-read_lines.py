#!/usr/bin/python3
"""Module read n lines"""


def read_lines(filename="", nb_lines=0):
    """function read_lines"""

    with open(filename) as f:
        num = sum(1 for line in f)
        if nb_lines <= 0 or nb_lines >= num:
            for lines in f:
                print(lines, end="")
        else:
            for lines in range(nb_lines):
                print(f.readline(), end="")
