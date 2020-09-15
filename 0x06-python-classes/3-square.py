#!/usr/bin/python3
"""square3"""


class Square:
    """Area of a square"""
    def __init__(self, size=0):
        self.__size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Area function"""
        return self.__size*self.__size
