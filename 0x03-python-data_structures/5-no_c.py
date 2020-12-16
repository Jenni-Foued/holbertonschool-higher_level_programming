#!/usr/bin/python3


def no_c(my_string):
    str = ""
    for index in range(0, len(my_string)):
        if (my_string[index] != 'c') and (my_string[index] != 'C'):
            str = str + my_string[index]
    return str
