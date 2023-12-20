#!/usr/bin/python3
"""Define a getter and setter for a size."""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """__init__ method.

        Args:
            size (int, optional): length of the side of a square
        """
        self.__size = size

    @property
    def size(self):
        """Get the length of the side of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square"""
        return self.size * self.size

    def __eq__(self, other):
        """Implement == comparison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Implement != comparison"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Implement > comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Implement >= comparison"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Implement < comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """Implement <= comparison"""
        return self.area() <= other.area()
