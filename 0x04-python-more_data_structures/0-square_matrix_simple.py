#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for element in matrix:
        a = [num**2 for num in element]
        mat.append(a)
    return mat
