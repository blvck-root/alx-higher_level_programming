#!/usr/bin/python3
"""Define a method names area to find the square."""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """__init__ method.

        Args:
            size (int, optional): length of the side of a square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square"""
        return self.__size * self.__size
