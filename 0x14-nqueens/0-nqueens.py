#!/usr/bin/python3
"""module"""


from sys import argv
if len(argv) > 2:
    print('Usage: nqueens N')
    exit(1)
try:
    N = int(argv[1])
except ValueError:
    print('N must be an integer')
    exit(1)
if N < 4:
    print('N must be at least 4')
    exit(1)


def printSolution(board):
    ls = []
    for i, v in enumerate(board):
        for j in range(len(v)):
            if board[i][j] == 1:
                ls.append([i, j])
    print(ls)


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i]:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while j >= 0 and i < N:
        if board[i][j]:
            return False
        i = i + 1
        j = j - 1
    return True


def solveNQUtil(board, col):
    if col == N:
        printSolution(board)
        return True
    res = False
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[i][col] = 0
    return res


def solveNQ():
    board = [[0 for j in range(N)]
             for i in range(N)]
    if not solveNQUtil(board, 0):
        print("Solution does not exist")
        return
    return


solveNQ()
