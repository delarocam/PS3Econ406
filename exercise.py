"""This document is for generating matrices of various specifications"""
import timeit
import numpy as np
# 1.)


def generate_s_matrix(number: int):
    """creates an s matrix with ones around the border"""
    matrix_zero = np.ones((number, number))
    matrix_zero[1:-1, 1:-1] = 0
    return matrix_zero

# test:
# generate_s_matrix(5)


# 2.)


def generate_matrix(rows, cols):
    """generates a random matrix with specified rows and columns"""
    matrix_random = np.random.rand(rows, cols)
    return matrix_random


# test
# generate_matrix(5, 3)

# 3.)


def matrix_multiplication_loop(x_matrix, y_matrix):
    """Multiplies x and y using a manual forloop"""
    result = []
    for i, row in enumerate(x_matrix):
        row_vector = []
        for j in range(len(y_matrix[0])):
            product = 0
            for k in range(len(row)):
                product += x_matrix[i][k] * y_matrix[k][j]
            row_vector.append(product)
        result.append(row_vector)
    return result


# test: to see if gets same result as np.dot

# matrix_a = generate_matrix(2, 3)
# matrix_b = generate_matrix(3, 2)
# print(matrix_multiplication_loop(matrix_a, matrix_b))
# print(np.dot(matrix_a, matrix_b))

# 4.)

matrix_1 = generate_matrix(10, 10)
matrix_2 = generate_matrix(10, 10)
matrix_3 = generate_matrix(100, 100)
matrix_4 = generate_matrix(100, 100)


def timed_multiplication_loop(x_matrix, y_matrix):
    '''Times how long it takes to multiply x and y.
       100 matrix time: [0.8300021 seconds]
       10 matrix time: [0.000894 seconds]
    '''
    setup = "from __main__ import matrix_multiplication_loop"
    result = matrix_multiplication_loop(x_matrix, y_matrix)
    time = timeit.timeit(stmt="matrix_multiplication_loop(x_matrix, y_matrix)",
                         setup=setup, globals=locals(), number=1)
    print(time)
    return result


# test


# timed_multiplication_loop(matrix_1, matrix_2)
# timed_multiplication_loop(matrix_3, matrix_4)


# 5.)

def timed_multiplication_numpy(x_matrix, y_matrix):
    '''Times how long it takes to multiply x and y.
       100 matrix time: [0.0001189999 seconds]
       10 matrix time: [2.3099 e-05 seconds]
    '''
    result = np.dot(x_matrix, y_matrix)
    setup = "import numpy as np"
    time = timeit.timeit(stmt="np.dot(x_matrix, y_matrix)",
                         setup=setup, globals=locals(), number=1)
    print(time)
    return result


# test
# timed_multiplication_numpy(matrix_1, matrix_2)
# timed_multiplication_numpy(matrix_3, matrix_4)
