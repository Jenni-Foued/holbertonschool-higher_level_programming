#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class Square
    Attributes:
        __size (int): size of a side of the square"""
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
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, new_size):
        """setter of __size
        Args:
            new_size (int): the size of a size of the square
        """
        if type(new_size) is not int:
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, new_size):
        """setter of __size
        Args:
            new_size (int): the size of a size of the square
        """
        if type(new_size) is not int:
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for column in range(self.__size):
                for pos in range(self.__position[0]):
                    print(" ", end="")
                for row in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def position(self):
        """getter of __position
        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): position of the square"""
        if type(value) is not tuple or len(value) != 2 or
           type(value[0]) is not int or value[0] < 0 or
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
