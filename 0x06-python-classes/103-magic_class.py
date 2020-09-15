#!/usr/bin/python3
"""magicclass"""


class MagicClass:
    """whatevr"""

    def __init__(self, radius=0):
        """init"""
        self.radius = 0
        if not type(radius) is int and not type(radius) is float:
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """area"""
        return (self.radius ** 2)*math.pi

    def circumference(self):
        """circumference"""
        return 2*math.pi*self.radius
