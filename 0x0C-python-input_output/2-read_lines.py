#!/usr/bin/python3
"""Module read n lines"""


def read_lines(filename="", nb_lines=0):
    """function read_lines"""

    with open(filename) as f:
        if nb_lines <= 0:
            for line in f:
                print(line, end="")
        else:
            head = [next(f) for x in range(nb_lines)]
            print(''.join(head))
