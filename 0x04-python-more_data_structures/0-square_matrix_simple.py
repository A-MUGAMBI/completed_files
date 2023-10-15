#!/usr/bin/python3

"""a program that computes all the value of integers"""

def square_matrix_simple(matrix=[]):
    square_matrix = []
    for line in matrix:
        line_let = []
        for item in line:
            line_let.append(item ** 2)
        square_matrix.append(line_let)
    return (square_matrix)
