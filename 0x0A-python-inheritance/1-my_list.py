#!/usr/bin/python3
"""
Defines  Mylist class
"""


class Mylist(list):
    """
    list subclass
    """

    def print_sorted(self):
        """
        prints the list sorted (ascending sort)
        """
        print(sorted(self))
