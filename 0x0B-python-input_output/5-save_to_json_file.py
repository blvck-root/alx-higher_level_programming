#!/usr/bin/python3

"""
The 5-save_to_json_file module contains the function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a file using JSON representation"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
