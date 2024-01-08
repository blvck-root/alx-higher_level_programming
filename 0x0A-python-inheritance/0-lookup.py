#!/usr/bin/python3

"""The 0-lookup module has a function that lists attributes of a class.
"""


def lookup(obj):
    """Lists all the attributes and methods of an object.

    Args:
      obj: object

    Returns:
      List of attributes and methods of an object.
    """
    return dir(obj)
