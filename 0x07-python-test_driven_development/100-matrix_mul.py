#!/usr/bin/python3
"""
This module multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ This function takes 2 matrices
        checks them, and multiplies them
        if possible """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not all(type(i) is list for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(i) is list for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a in [[], [[]]]:
        raise ValueError("m_a can't be empty")
    if m_b in [[], [[]]]:
        raise ValueError("m_b can't be empty")
    if not all(all(type(j) in [int, float] for j in i) for i in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(type(j) in [int, float] for j in i) for i in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(i) == len(m_a[0]) for i in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(i) == len(m_b[0]) for i in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if not len(m_a[0]) == len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[0 for i in m_b[0]] for j in m_a]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
