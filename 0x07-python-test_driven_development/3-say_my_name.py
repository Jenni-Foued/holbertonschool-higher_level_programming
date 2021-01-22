#!/usr/bin/python3
"""
"Say my name" module

This module supplies one function say_my_name():
    it prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
        Prints My name is <first name> <last name>

        Args:
            first_name (str): first name
            last_name (str): last name
        Raises:
            TypeError: in case one or both arguments type is not string
        Return:
            Nothing to return.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
