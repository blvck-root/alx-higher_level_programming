#!/usr/bin/python3

"""
The 4-print_square module prints a square.

>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """
    Prints a string representation of a square.

    Args:
      size: integer length of square

    Returns:
      None

    Raises:
      TypeError: If size is not an integer or size is a negative float
      ValueError: If size is less than 0

    Example:
      >>> print_square(4)
      ####
      ####
      ####
      ####
    """

    if type(size) is not int and size != 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    # square is a (size x size) grid made from the # character
    square = ""
    for i in range(size):
        square += "#" * size + "\n"
    if len(square) > 0:
        print(square, end="")
