#!/usr/bin/python3

"""4-inherits_from module checks if an object is an instance of a subclass.
"""


def inherits_from(obj, a_class):
    """Checks if 'obj' is an instance of a subclass of 'a_class'.

    Args:
      obj: object
      a_class: class

    Returns:
      True if obj is an instance of a subclass of a_class, else False
    """
    return isinstance(obj, a_class) and not (type(obj) is a_class)
