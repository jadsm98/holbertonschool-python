#!/usr/bin/python3
"""Square6"""


class Square:
    """coordinate of a square"""
    def __init__(self, size=0, position=(0, 0)):
        """init"""
        self.size = size
        self.position = position

    def __str__(self):
        """to print"""
        return self.my_print()

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
        if type(value) is not tuple or len(value) \
           != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            result += '\n'*self.__position[1]
            result += ' '*self.__position[0]
            result += '#'*self.__size
            for i in range(self.__size - 1):
                result += '\n'
                result += ' '*self.__position[0]
                result += '#'*self.__size
        return result
