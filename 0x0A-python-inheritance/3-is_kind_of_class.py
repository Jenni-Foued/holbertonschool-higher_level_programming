#!/usr/bin/python3
"""
"Kind of class" module

This module provides one function is_kind_of_class()
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of a class;
    otherwise False."""
    return isinstance(obj, a_class)
