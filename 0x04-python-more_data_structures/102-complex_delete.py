#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary.keys())
    for key in key_list:
        if a_dictionary.get(key) == value:
            del a_dictionary[key]
    return a_dictionary
