#!/usr/bin/python3
"""
The 8-rectangle module contains a Rectangle class.
"""


class Rectangle:
    """Blueprint for Rectanlge objects.

    Attributes:
        number_of_instances: number of instances created
        print_symbol: symbol for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__ method.

        Args:
            width (optional): width of a rectangle
            height (optional): height of a rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of a rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of a rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of a rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of a rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of a rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of a rectangle."""
        return 2 * (self.width + self.height)

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the biggest area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return max(rect_1, rect_2, key=lambda x: x.area())

    def __str__(self):
        """Return string representation of a rectangle."""
        if self.width == 0 or self.height == 0:
            return ""

        symbol = str(self.print_symbol)
        string = (symbol*self.width + "\n") * self.height
        return string[:-1]

    def __repr__(self):
        """Return string representation of a rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Handle instance deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
