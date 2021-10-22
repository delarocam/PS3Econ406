"""This document is for generating matrices of various specifications"""
import numpy as np

# 1.)


def generate_s_matrix(n):
    matrix_zero = np.ones((n, n))
    matrix_zero[1:-1, 1:-1] = 0
    print(matrix_zero)
    return matrix_zero

# test:
# generate_s_matrix(5)


# 2.)


def generate_matrix(rows, cols):
    matrix_random = np.random.rand(rows, cols)
    print(matrix_random)
    return matrix_random


# test
# generate_matrix(5, 3)

# 3.)


def matrix_multiplication_loop(x, y):
    """Multiplies x and y using a manual forloop"""
    result = []
    for i in range(len(x)):
        row = []
        for j in range(len(y[0])):
            product = 0
            for k in range(len(x[i])):
                product += x[i][k] * y[k][j]
            row.append(product)
        result.append(row)
    return result


# test
# matrix_multiplication_loop(generate_matrix(2, 3), generate_matrix(3, 2))

# 4.)
