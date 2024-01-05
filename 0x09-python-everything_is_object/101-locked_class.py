#!/usr/bin/python3
"""
101-locked_class module contains the LockedClass.
"""

class LockedClass:
    """Blueprint for the LockedClass class."""
    def __setattr__(self, name, value):
        """This function is called when a new instance attribute is set."""
        if name != "first_name":
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        self.__dict__[name] = value
