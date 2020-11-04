#!/usr/bin/python3
"""module"""


def rotate_2d_matrix(matrix):
    """function"""

    new_matrix = [[j for j in i] for i in matrix]
    for i, v in enumerate(matrix):
        for j in range(len(v)):
            matrix[i][j] = new_matrix[len(matrix)-1-j][i]
