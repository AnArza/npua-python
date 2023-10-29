from lec_6.matrix_operations import generate_random_matrix


class Matrix:
    def __init__(self, n, m):
        if n <= 0 or m <= 0:
            raise ValueError('Matrix dimensions n and m must be positive integers.')
        self.matrix = generate_random_matrix(n, m)

    def print_matrix(self):
        for row in self.matrix:
            for elem in row:
                print(f' {elem:>3} ', end='')
            print()

    def mean(self):
        total_sum = sum(sum(row) for row in self.matrix)
        return total_sum / (len(self.matrix) * len(self.matrix[0]))

    def row_sum(self, row):
        if 0 <= row < len(self.matrix):
            return sum(self.matrix[row])
        else:
            raise ValueError(f'Row index {row} out of bounds.')

    def column_average(self, col):
        if 0 <= col < len(self.matrix[0]):
            col_sum = sum(self.matrix[row][col] for row in range(len(self.matrix)))
            return col_sum / len(self.matrix)
        else:
            raise ValueError(f'Column index {col} out of bounds.')

    def submatrix(self, col1, col2, row1, row2):
        if col1 < 0 or col2 >= len(self.matrix[0]) or col1 > col2:
            raise ValueError(f'Column indices {col1} and {col2} are out of bounds or invalid.')
        if row1 < 0 or row2 >= len(self.matrix) or row1 > row2:
            raise ValueError(f'Row indices {row1} and {row2} are out of bounds or invalid.')

        result = []
        for row in range(row1, row2 + 1):
            result.append(self.matrix[row][col1:col2 + 1])
        return result
