#!/usr/bin/python3
"""Module my_int"""


class MyInt(int):
    """class MyInt """
    def __eq__(self, value):
        return False

    def __ne__(self, value):
        return True
