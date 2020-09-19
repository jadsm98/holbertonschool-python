#!/usr/bin/python3
"""
Lazy matrix multiplication module
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Takes 2 matrices and returns their
        multiplication if possible using
        NumPy """
    if type(m_a) is not list:
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    if type(m_b) is not list:
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    if not all(type(i) is list for i in m_a):
        raise ValueError("m_a can only be a matrix")
    if not all(type(i) is list for i in m_b):
        raise ValueError("m_b can only be a matrix")
    if m_a in [[], [[]]]:
        raise ValueError("m_a cannot be of dimension 0")
    if m_b in [[], [[]]]:
        raise ValueError("m_b cannot be of dimension 0")
    if not all(all(type(j) in [int, float] for j in i) for i in m_a):
        raise ValueError("invalid data type for einsum")
    if not all(all(type(j) in [int, float] for j in i) for i in m_b):
        raise ValueError("invalid data type for einsum")
    if not all(len(i) == len(m_a[0]) for i in m_a):
        raise TypeError("setting an array element with a sequence")
    if not all(len(i) == len(m_b[0]) for i in m_b):
        raise TypeError("setting an array element with a sequence")
    if not len(m_a[0]) == len(m_b):
        raise ValueError("size of m_a is different than size of m_b")

    return np.matmul(m_a, m_b)    
