#!/usr/bin/python3
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
        """Get the length of a the side of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square"""
        return self.size * self.size

    def my_print(self):
        """Print square."""
        if self.size == 0:
            print("")

        for i in range(self.size):
            print("#" * self.size)
