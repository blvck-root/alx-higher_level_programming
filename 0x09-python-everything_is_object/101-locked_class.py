#!/usr/bin/python3
"""
101-locked_class module contains the LockedClass.
"""


class LockedClass:
    """Blueprint for the LockedClass class."""
    __slots__ = ("first_name",)

    def __setattr__(self, name, value):
        """This function is called when a new instance attribute is set."""
        if name != "first_name":
            raise AttributeError(
                f"'LockedClass' object has no attribute '{name}'"
            )
        super().__setattr__(name, value)
