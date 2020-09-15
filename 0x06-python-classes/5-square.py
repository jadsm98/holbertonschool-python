#!/usr/bin/python3
"""square5"""


class Square:
    """square representation"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self,value):
        """setter"""
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area"""
        return self.__size*self.__size

    def my_print(self):
        """prints square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('{}'.format('#'), end='')
                print()
