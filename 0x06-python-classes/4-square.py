#!/usr/bin/python3
"""square4"""


class Square:
    """getters/setters"""
    def __init__(self, size=0):
        self.size = size

    @property    
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def area(self):
        """Area"""
        return self.__size*self.__size
