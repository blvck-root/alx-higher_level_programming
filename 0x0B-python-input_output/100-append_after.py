#!/usr/bin/python3

"""100-append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts line of text after each line containing a specific string
    """
    match_indexes = []

    with open(filename, 'r', encoding='utf-8') as file:
        contents = file.readlines()

        for i in range(len(contents)):
            if search_string in contents[i]:
                contents.insert(i + 1, new_string)

    with open(filename, 'w', encoding='utf-8') as file:
        contents = "".join(contents)
        file.write(contents)
