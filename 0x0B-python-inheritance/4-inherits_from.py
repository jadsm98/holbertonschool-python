#!/usr/bin/python3
"""Module inherits_from"""


def inherits_from(obj, a_class):
    """function inherits_from"""

    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
