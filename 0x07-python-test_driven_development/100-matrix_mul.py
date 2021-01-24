#!/usr/bin/python3
"""
"Matrix multiplication" module

This module provides one function matrix_mul(): multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices

    Args:
        m_a (list): first matrice
        m_b (list): second matrice

    Return:
        m_c (list): the result matrice
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for elm in m_a:
        if type(elm) is not list:
            raise TypeError("m_a must be a list of lists")

    for elm in m_b:
        if type(elm) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for elm in m_a:
        for nb in elm:
            if type(nb) not in [float, int]:
                raise TypeError("m_a should contain only integers or floats")

    for elm in m_b:
        for nb in elm:
            if type(nb) not in [float, int]:
                raise TypeError("m_b should contain only integers or floats")

    len_m = None
    for elm in m_a:
        if len_m is None:
            len_m = len(elm)
        if len(elm) != len_m:
            raise TypeError("each row of m_a must be of the same size")

    len_m = None
    for elm in m_b:
        if len_m is None:
            len_m = len(elm)
        if len(elm) != len_m:
            raise TypeError("each row of m_b must be of the same size")
    m_c = [[]]
    return m_c
