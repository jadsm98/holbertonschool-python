#!/usr/bin/python3
""" Module square 1"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def integer_validator(self, name, value):
        return super().integer_validator(name, value)

    def area(self):
        return self.__size*self.__size
