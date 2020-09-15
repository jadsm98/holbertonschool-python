#!/usr/bin/python3
"""MagicClass"""


class MagicClass:
    """Translation:
        from bytecode to code"""
    def __init__(self, radius=0):
        """init"""
        self.__radius = 0
        if not type(radius) is int and not type(radius) is float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area"""
        return math.pi*self.__radius ** 2

    def circumference(self):
        """circumference"""
        return 2*math.pi*self.__radius
