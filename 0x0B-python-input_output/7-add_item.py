#!/usr/bin/python3

"""
The 7-add_item module adds all arguments to a list and saves to a file
"""
import sys
save_f = __import__('5-save_to_json_file').save_to_json_file
load_f = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    my_list = load_f(filename)
except FileNotFoundError:
    my_list = []

my_list.extend(sys.argv[1:])
save_f(my_list, filename)
