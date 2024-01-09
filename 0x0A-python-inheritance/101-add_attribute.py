#!/usr/bin/python3

"""The 101-add_attribute module."""


def add_attribute(obj, name, value):
    """Adds attribute if possible

    Raises:
      TypeError: if attribute can't be added
    """
    if (
        hasattr(obj.__class__, "__slots__") and
        name in getattr(obj.__class__, "__slots__")
       ):
        setattr(obj, name, value)
    elif hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
