#!/usr/bin/python3

"""
0-read_file module contains read_file function
"""

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
