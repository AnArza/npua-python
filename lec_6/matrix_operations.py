import random


def generate_random_matrix(rows, cols):
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]


def get_column_sum(matrix, col):
    if not matrix or col < 0 or col >= len(matrix[0]):
        raise ValueError("Invalid matrix or column index")

    return sum(row[col] for row in matrix)


def get_row_average(matrix, row):
    if not matrix or row < 0 or row >= len(matrix):
        raise ValueError("Invalid matrix or row index")

    return sum(matrix[row]) / len(matrix[row])
