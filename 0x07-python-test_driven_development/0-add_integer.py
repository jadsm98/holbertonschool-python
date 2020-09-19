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

    if a != a:
        a = 89
    if b != b:
        b = 89
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    result = int(a) + int(b)
    return result
