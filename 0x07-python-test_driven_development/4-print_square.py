#!/usr/bin/python3
"""
Module that contains print_square function
that prints a square using #
"""


def print_square(size):
    """ This function takes the size of the  square
        and prints it using # """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
