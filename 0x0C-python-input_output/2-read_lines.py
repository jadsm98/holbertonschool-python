#!/usr/bin/python3
"""Module read n lines"""


def read_lines(filename="", nb_lines=0):
    """function read_lines"""

    with open(filename) as f:
        for lines in f:
            print(lines, end="")
            if lines == nb_lines:
                if nb_lines > 0 or nb_lines < len(f): 
                    break
