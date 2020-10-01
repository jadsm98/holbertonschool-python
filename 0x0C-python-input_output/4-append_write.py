#!/usr/bin/python3
"""module append_write"""


def append_write(filename="", text=""):
    """function append_write"""

    with open(filename, "a+") as f:
        return f.write(text)
