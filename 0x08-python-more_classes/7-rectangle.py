#!/usr/bin/python3
"""Module 7-rectangle"""


class Rectangle:
    """ class rectangle7 """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width*self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            rep = ''
            for i in range(self.__width):
                rep += str(self.print_symbol)
            for i in range(self.__height - 1):
                rep += '\n'
                for j in range(self.__width):
                    rep += str(self.print_symbol)
        return rep

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + \
                ', ' + str(self.__height) + ")"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
