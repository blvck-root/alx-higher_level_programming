#!/usr/bin/python3

"""
The 3-say_my_name module contains the function say_my_name
>>> say_my_name("Mvuyisi", "Mdingi")
My name is Mvuyisi Mdingi
"""


def say_my_name(first_name, last_name=""):
    """
    Prints name and surname.

    Args:
        first_name: string
        last_name: string (optional)

    Returns:
        None

    Raises:
        TypeError: If first_name or last_name is not a string
        TypeError: If first_name is missing

    Example:
        >>> say_my_name("Mvuyisi", "Mdingi")
        My name is Mvuyisi Mdingi
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
