#!/usr/bin/python3
"""
Defines  Mylist class
"""


class MyList(list):
    """list subclass"""
    def __init__(self):
        """initializes the list"""
        super().__init__()

    def print_sorted(self):
        """prints the list sorted (ascending sort)"""
        print(sorted(self))
