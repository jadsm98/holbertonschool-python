#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    size = len(matrix)
    new_matrix = [[0 for x in range(size)] for y in range(size)]
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            new_matrix[i][j] = col*col
    return new_matrix
