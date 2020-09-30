#!/usr/bin/python3
""" Module square 1"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        Rectangle.integer_validator(self, "size", size)

    def area(self):
        return self.__size*self.__size
