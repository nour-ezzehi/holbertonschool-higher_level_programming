#!/usr/bin/python3
"""Text Indention"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters:
        ., ? and :"""

    if type(text) is not str:
        raise TypeError('text must be a string')
    i = 0
    while i < len(text):
        if text[i] in [':', '.', '?']:
            print(text[i])
            print()
            i += 1
        else:
            print(text[i], end='')
        i += 1
