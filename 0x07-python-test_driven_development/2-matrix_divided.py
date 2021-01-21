#!/usr/bin/python3
"""
"2-matrix_divided" module.

This module supplies one function, matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix by div

        Args:
            matrix (list): matrix (list of lists) of integers/floats
            div (integer/float): diviser of the matrix
        Raises:
            ...
        Returns:
            (list): a new matrix (matrix divided by div)
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    size = None
    for sub_list in matrix:
        if type(sub_list) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if size is None:
            size = len(sub_list)
        elif size != len(sub_list):
            raise TypeError("Each row of the matrix must have the same size")
        for elm in sub_list:
            if type(elm) is not int and type(elm) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elm / div, 2) for elm in sub_list] for sub_list in matrix]
