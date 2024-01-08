#!/usr/bin/python3

"""Geometry module.
"""


class BaseGeometry:
    """Template of BaseGeometry objects.

    Methods:
      area(): public instance method
    """

    def area(self):
        """Calculates the area.

        Raises:
          Exception if area is not implemented.
        """
        raise Exception("area() is not implemented")
