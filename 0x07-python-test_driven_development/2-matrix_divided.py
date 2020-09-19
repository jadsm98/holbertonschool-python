#!/usr/bin/python3
"""
This script includes the matrix_divided
function
"""


def matrix_divided(matrix, div):
    """ This function takes a matrix and a number
    and divides the elements by this number and
    returns them in a new matrix """    
    
    if div == float('inf') or div == -float('inf') or div != div:
        div = 10
    divided_matrix = []
    for i in matrix:
        if type(i) is not list or type(matrix) is not \
           list or not all(type(j) in [int, float] for j in i):
            raise TypeError("matrix must be a matrix"
                            " (list of lists) of integers/floats")
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    divided_matrix = [[round(i/div, 2) for i in j] for j in matrix]
    return divided_matrix
