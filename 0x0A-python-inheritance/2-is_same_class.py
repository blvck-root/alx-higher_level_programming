#!/usr/bin/python3

"""2-is_same_class module checks if an object
   is exactly an instance of a class.
"""


def is_same_class(obj, a_class):
    """Checks if 'obj' is exactly an instance of 'a_class'.

    Args:
      obj: object
      a_class: class

    Returns:
      True if obj is exactly an instance of a_class, else False
    """
    return type(obj) is a_class
