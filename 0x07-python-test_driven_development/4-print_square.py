#!/usr/bin/python3
"""
"Print square" module

This module supplies one function print_square():
    prints a square with the character #.
"""


def print_square(size):
    """
        Prints a square

        Args:
            size (int): size of a side of the square
        Raises:
            TypeError: in case size is not int.
            ValueError: in case size less than 0.
        Return:
            Nothing to return.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        print(("#" * size + '\n') * size, end="")
