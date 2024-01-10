#!/usr/bin/python3
"""Geometry module.
"""


class BaseGeometry(object):
    """Template of BaseGeometry objects.

    Methods:
      area: public instance method
      integer_validator: validates a number
    """

    def area(self):
        """Calculates the area.

        Raises:
          Exception if area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.

        Args:
          name: string
          value: number to be validated

        Raises:
          TypeError: If value is not an integer
          ValueError: If value <= 0

        Returns:
          None
        """
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
