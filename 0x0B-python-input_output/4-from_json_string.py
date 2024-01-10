#!/usr/bin/python3
import json

"""
The 4-from_json_string module contains the from_json_string function
"""


def from_json_string(my_str):
    """Returns an object from a JSON string"""
    return json.loads(my_str)
