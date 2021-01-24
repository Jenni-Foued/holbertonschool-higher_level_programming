#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Class Rectangle
    Attributes:
        __width (int): width of a side of the Rectangle"""

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        """setter of __width
        Args:
            new_width (int): the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        """setter of __height
        Args:
            new_height (int): the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def __init__(self, width=0, height=0):
        """Initializes Rectangle's width and height
        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle"""
        self.__width = width
        self.__height = height
