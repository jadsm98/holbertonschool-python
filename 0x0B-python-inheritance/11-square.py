#!/usr/bin/python3
"""Module square2"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square2"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def integer_validator(self, name, value):
        return super().integer_validator(name, value)

    def area(self):
        return self.__size*self.__size

    def __repr__(self):
        return "[Square]" + str(self.__size) + "/" + str(self.__size)
