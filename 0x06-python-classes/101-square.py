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
            position (tuple): position of the square
        Returns:
            None
            """
        self.size = size
        self.position = position

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
                for pos0 in range(self.__position[0]):
                    print(' ', end="")
                for row in range(self.__size):
                    print('#', end="")
                print()
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
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
