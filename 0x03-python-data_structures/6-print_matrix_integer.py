#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print("{}".format(matrix[i][j]), end='')
            if j != (len(matrix) - 1):
                print("", end=' ')
        print()
