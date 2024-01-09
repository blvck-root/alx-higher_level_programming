#!/usr/bin/python3

"""100-my_int module"""


class MyInt(int):
    """Rebel version of int"""
    def __eq__(self, other):
        """Overrides equality"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Overrides not equal to"""
        return int.__eq__(self, other)
