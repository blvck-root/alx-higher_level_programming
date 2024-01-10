#!/usr/bin/python3

"""3-is_kind_of_class module checks if an object
   is an instance of the class or its descendants.
"""


def is_kind_of_class(obj, a_class):
    """Checks if 'obj' is an instance of 'a_class'.

    Args:
      obj: object
      a_class: class

    Returns:
      True if obj is an instance of a_class, else False
    """
    return isinstance(obj, a_class)
