#!/usr/bin/python3
"""
0-add_integer module includes function 
that takes 2 numbers a and b and returns
their addition
"""


def add_integer(a, b=98):
    """ Function that takes 2 numbers
    and returns their addition otherwise
    raises TypeError"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
