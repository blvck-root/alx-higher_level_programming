#!/usr/bin/python3

"""Square module.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class.

    Attributes:
      __size: private size attribute
    """
    def __init__(self, size):
        """Instantiates Square class with private __size attribute."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
