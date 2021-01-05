#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class Square
    Attributes:
        __size (int): size of a side of the square
        __position (tuple): position of the square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes square's size
        Args:
            size (int): size of a side of the square
            position (tuple): position of the square"""
        self.__size = size
        self.__position = position

    def area(self):
        """Calculates the square's area
        Returns:
            The square area"""
        return self.__size ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size > 0:
            for pos1 in range(self.__position[1]):
                print()
            for column in range(self.__size):
                print("".join([" " for j in range(self.__position[0])]),
                      end="")
                print("".join(["#" for row in range(self.__size)]))
        else:
            print()

    @property
    def position(self):
        """getter of __position
        Returns:
            The position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): position of the square"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
