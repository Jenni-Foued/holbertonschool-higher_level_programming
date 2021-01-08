#!/usr/bin/python3
"""
Add module

This module supplies one function, add_integer(): it adds to numbers
"""

def add_integer(a, b=98):
    """
        Sum of a and b

        Args:
            a (int/float): first number
            b (int/float): second number
        Raises:
            TypeError: in case of the arguments given or both aren't
                        int/float
        Returns:
            (int) : The sum of a and b
        """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        int(a)
    if type(b) is float:
        int(b)
    return a + b
