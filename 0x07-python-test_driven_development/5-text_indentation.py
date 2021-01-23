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
        eol = False
        for elm in range(0, len(text)):
            if text[elm] == '.' or text[elm] == '?':
                print (text[elm] + "\n")
                eol = True
            elif eol == False:
                print(text[elm], end="")
            else:
                eol = False
