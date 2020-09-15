#!/usr/bin/python3
"""Square6"""


class Square:
    """coordinate of a square"""
    def __init__(self, size=0, position=(0, 0)):
        """init"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if isinstance(value, tuple) and list(map(type, value)) == [int, int] \
           and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @size.setter
    def size(self, value):
        """setter for size"""
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
            print('\n'*self.__position[1], end='')
            for i in range(self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size, end='')
                print()
