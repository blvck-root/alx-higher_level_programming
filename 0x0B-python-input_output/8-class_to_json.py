#!/usr/bin/python3

"""The 8-class_to_json.py module"""


def class_to_json(obj):
    """Returns dictionary for JSON serialization"""
    return obj.__dict__
