#!/usr/bin/python3
"""Decode Python ByteCode"""


import math


class MagicClass:
    """Define MagicClass"""
    def __init__(self, radius):
        """Initialize MagicClass"""
        self.radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        return self.radius**2 * math.pi

    def circumference(self):
        return 2*math.pi * self.radius
