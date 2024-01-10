#!/usr/bin/python3
"""
The 5-text_indetation module contains the text_indentation function.
>>> text_indentation("Si id dicis, vicimus. Sin aliud quid voles, postea")
Si id dicis, vicimus.
<BLANKLINE>
Sin aliud quid voles, postea
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each delimiter ('.', '?', ':')

    Args:
      text: string

    Returns:
      None

    Raises:
      TypeError: If text is not a string

    Example:
      >>> text_indentation("Si id dicis. Sin vicimus")
      Si id dicis.
      <BLANKLINE>
      Sin vicimus
    """

    line = ""
    delim = (".", "?", ":")

    if type(text) is not str:
        raise TypeError("text must be a string")

    if text.isspace() or text == "":
        print("", end="")
        return

    i = 0
    trimmed_text = text.strip()
    text_length = len(trimmed_text)
    while i < text_length:
        if trimmed_text[i] in delim:
            # print text with two new lines
            print(line + trimmed_text[i] + "\n")
            line = ""
            i += 1
            while i < text_length and trimmed_text[i].isspace():
                i += 1
        else:
            line += trimmed_text[i]
            i += 1
    print(line, end="")
