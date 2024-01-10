#!/usr/bin/python3

"""
The 0-add_integer module contains a function that adds two integers.
>>> add_integer(2, 3)
5
"""


def add_integer(a, b=98):
    """Return the integer sum of two numbers.
    >>> add_integer(0, -3)
    -3"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
