#!/usr/bin/python3

"""Rectangle module.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class is a subbclass of BaseGeometry.

    Attributes:
      __width: private width attribute
      __height: private height attribute
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
