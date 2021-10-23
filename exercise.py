"""This document is for generating matrices of various specifications"""
import numpy as np

import timeit
# 1.)


def generate_s_matrix(n):
    matrix_zero = np.ones((n, n))
    matrix_zero[1:-1, 1:-1] = 0
    return matrix_zero

# test:
# generate_s_matrix(5)


# 2.)


def generate_matrix(rows, cols):
    matrix_random = np.random.rand(rows, cols)
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

matrix_1 = generate_matrix(10, 10)
matrix_2 = generate_matrix(10, 10)
matrix_3 = generate_matrix(100, 100)
matrix_4 = generate_matrix(100, 100)


def timed_multiplication_loop(x, y):
    '''Times how long it takes to multiply x and y.
       10000 matrix time: [0.00027259 seconds]
       10 matrix time: [3.70 e-06 seconds]
    '''
    setup = "from __main__ import matrix_multiplication_loop"
    result = matrix_multiplication_loop(x, y)
    time = timeit.timeit(stmt=str(matrix_multiplication_loop(x, y)),
                         setup=setup,
                         number=1)
    print(time)
    return result


# test


# timed_multiplication_loop(matrix_1, matrix_2)
# timed_multiplication_loop(matrix_3, matrix_4)


# 5.)

def timed_multiplication_numpy(x, y):
    '''Times how long it takes to multiply x and y.
       10000 matrix time: [YOUR TIME HERE]
       10 matrix time: [YOUR TIME HERE]
    '''
    result = np.dot(x, y)
    setup = "import numpy as np"
    time = timeit.timeit(stmt=str(np.dot(x, y)), setup=setup, number=1)
    print(time)
    return result


# test
# timed_multiplication_numpy(matrix_1, matrix_2)
# timed_multiplication_numpy(matrix_3, matrix_4)


print(str(np.dot(matrix_1, matrix_2)))
