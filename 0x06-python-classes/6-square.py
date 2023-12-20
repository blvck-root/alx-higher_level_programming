#!/usr/bin/python3
"""Define a square with position coordinates."""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method.

        Args:
            size (int, optional): length of the side of the square
            position (:obj: `tuple` of :obj: int, optional): square position
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple
                and len(value) != 2
                and type(value[0]) is not int
                and type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square"""
        return self.size * self.size

    def my_print(self):
        """Print square."""
        if self.size == 0:
            print("")

        for i in range(self.position[1]):
            print("")

        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
