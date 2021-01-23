#!/usr/bin/python3
"""
"Text indention" module

This module provides one function text_indention():
    prints a text with 2 new lines after each of these characters: ., ?
"""


def text_indentation(text):
    """
        Prints a text

        Args:
            text (str): text
        Raises:
            TypeError: in case text's type is not a string
        Return:
            Returns nothing
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        new_line = True
        for elm in range(0, len(text)):
            if new_line is True and text[elm] == ' ':
                print(end="")
            elif text[elm] == '.' or text[elm] == '?' or text[elm] == ':':
                print(text[elm] + "\n")
                new_line = True
            else:
                print(text[elm], end="")
                new_line = False
