#!/usr/bin/python3
"""square9"""


class Square:
    """comparing squares"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if not type(value) is int and not type(value) is float:
            raise TypeError("size must be an number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Area"""
        return self.__size*self.__size

    def __gt__(self, value):
        """greater than"""
        return self.area() > value.area()

    def __eq__(self, value):
        """equal"""
        return self.area() == value.area()

    def __ge__(self, value):
        """greater or equal"""
        return self.area() >= value.area()

    def __lt__(self, value):
        """less than"""
        return self.area() < value.area()

    def __le__(self, value):
        """less or equal"""
        return self.area() <= value.area()

    def __ne__(self, value):
        """not equal"""
        return self.area() != value.area()
