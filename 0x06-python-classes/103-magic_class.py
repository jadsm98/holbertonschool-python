#!/usr/bin/python3
"""magicclass"""


class MagicClass:
    """whatevr"""

    def __init__(self, radius=0):
        """init"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self, radius):
        """area"""
        return (self.__radius ** 2)*math.pi

    def circumference(self, radius):
        """circumference"""
        return 2*math.pi*self.__radius
