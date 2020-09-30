#!/usr/bin/python3
"""Module add_attribute"""


def add_attribute(obj, key, value):
    """ function that adds attributes"""

    if type(obj) in [int, float, complex, str, bool, \
                     range, frozenset, bytearray, memoryview, \
                     tuple, list, bytes, dict, set]:
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
