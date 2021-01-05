#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class Square
    Attributes:
        __size (int): size of a side of the square"""
    def __init__(self, size=0):
        """Initializes square's size
        Args:
            size (int): size of a side of the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the square's area
        Returns:
            The square area"""
        return self.__size ** 2
