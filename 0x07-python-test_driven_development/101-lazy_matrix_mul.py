#!/usr/bin/python3
import numpy as np
"""
"Lazy matrix multiplication" module
"""


def lazy_matrix_mul(m_a, m_b):
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

    len_m = m_a[0]
    for elm in m_a:
        if len(elm) != len_m:
            raise TypeError("each row of m_a must be of the same size")

    len_m = m_b[0]
    for elm in m_b:
        if len(elm) != len_m:
            raise TypeError("each row of m_b must be of the same size")

    m_c = np.matmul(m_a, m_b)
    return m_c
