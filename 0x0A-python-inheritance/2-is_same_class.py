#!/usr/bin/python3
"""
"Same class" module

This module provides one function is_same_class()
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified class
    ; otherwise False."""
    return type(obj) == a_class
