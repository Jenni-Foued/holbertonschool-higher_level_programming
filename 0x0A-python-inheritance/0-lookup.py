#!/usr/bin/python3


def lookup(obj):
    ''' returns the list of available attributes and methods of an object'''
    object_methods = [method_name for method_name in dir(obj)
                      if callable(getattr(obj, method_name))]
    return object_methods
