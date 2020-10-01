#!/usr/bin/python3
"""module"""


def append_after(filename="", search_string="", new_string=""):
    """function"""

    with open(filename) as f:
        lines = f.read().splitlines()
    with open(filename, "w") as f:
        for line in lines:
            if search_string in line:
                print(line + '\n'+ new_string, end="", file=f)
            else:
                print(line, file=f)
