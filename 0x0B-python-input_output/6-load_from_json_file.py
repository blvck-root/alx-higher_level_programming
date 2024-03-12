#!/usr/bin/python3

"""
The 6-load_from_json_file module contains the function load_from_json_file
"""
import json


def load_from_json_file(filename):
    """Writes an object to a file using JSON representation"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
