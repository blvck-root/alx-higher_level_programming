#!/usr/bin/python3

"""The 2-append_write module containts the append_write function"""


def append_write(filename="", text=""):
    """Appendss to a file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
