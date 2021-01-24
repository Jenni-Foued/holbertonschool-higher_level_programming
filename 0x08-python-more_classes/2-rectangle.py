#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Class Rectangle
    Attributes:
        __width (int): width of the Rectangle
        __height (int): height of the Rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializes Rectangle's width and height
        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter of __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of __width
        Args:
            value (int): the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter of __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of __height
        Args:
            value (int): the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the rectangle's area"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
