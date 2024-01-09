#!/usr/bin/python3

"""The '1-my_list' module contains the 'MyList' class.
"""


class MyList(list):
    """MyList is a subclass of the 'list' class.

    Methods:
      print_sorted: prints list items in sorted order
    """

    def print_sorted(self):
        """Print list in ascending order."""
        print(sorted(self))
