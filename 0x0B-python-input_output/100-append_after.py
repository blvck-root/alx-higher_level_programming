#!/usr/bin/python3

"""100-append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts line of text after each line containing a specific string
    """

    with open(filename, 'r', encoding='utf-8') as file:
        new_text = ""
        for line in file:
            new_text += line
            if search_string in line:
                new_text += new_string

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(new_text)
