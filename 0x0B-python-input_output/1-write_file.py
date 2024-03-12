#!/usr/bin/python3

"""
The 1-write_file module containts the write_file function
"""


def write_file(filename="", text=""):
    """Writes to a file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
