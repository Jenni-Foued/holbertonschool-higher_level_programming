#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except IndexError as ierr:
        print("Exception: {}".format(ierr), file=sys.stderr)
        result = None
    except ZeroDivisionError as derr:
        print("Exception: {}".format(derr), file=sys.stderr)
        result = None
    return result
