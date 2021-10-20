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
