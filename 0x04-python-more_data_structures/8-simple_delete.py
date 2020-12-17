#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    try:
        del a_dictionary[key]
    except:
        pass
    return a_dictionary
