#!/usr/bin/python3

"""Rectangle module.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class is a subclass of BaseGeometry.

    Attributes:
      __width: private width attribute
      __height: private height attribute
    """
    def __init__(self, width, height):
        """Instatiates the Rectangle class

        Args:
          width: width of rectangle
          height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of a rectangle.

        Returns:
          Area of rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """String representation of a rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
