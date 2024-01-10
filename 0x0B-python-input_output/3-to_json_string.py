#!/usr/bin/python3
import json

"""
The 3-to_json_string module contains the to_json_string function
"""


def to_json_string(my_obj):
    """Returns JSON representation of an object"""
    return json.dumps(my_obj)
