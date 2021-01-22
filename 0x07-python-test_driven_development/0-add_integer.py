#!/usr/bin/python3
"""
"0-add_integer" module

This module supplies one function, add_integer(): it adds two numbers
"""


def add_integer(a, b=98):
    """
        Adds 2 integers.

        Args:
            a (int/float): first number
            b (int/float): second number
        Raises:
            TypeError: in case of the arguments given or both aren't
                        int/float
        Returns:
            (int) : The sum of a and b
        """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
