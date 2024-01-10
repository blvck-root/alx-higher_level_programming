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
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the length of a the side of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
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
        """Set the position of the square"""
        if (type(value) is not tuple
                or len(value) != 2
                or type(value[0]) is not int
                or type(value[1]) is not int
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square"""
        return self.size * self.size

    def my_print(self):
        """Print square."""
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")

            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)

    def __repr__(self):
        """String representation of square."""
        string = ""
        if self.size > 0:
            for i in range(self.position[1]):
                string += "\n"

            for i in range(self.size):
                string += " "*self.position[0] + "#"*self.size + "\n"
        return string[:-1]
