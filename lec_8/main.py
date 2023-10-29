from matrix import Matrix


matrix = Matrix(3, 3)
matrix.print_matrix()

print(f'Mean of the matrix: {matrix.mean()}')

print(f'Sum of the second row: {matrix.row_sum(1)}')

print(f'Average of the second column: {matrix.column_average(1)}')

submatrix = matrix.submatrix(1, 2, 1, 2)
matrix.matrix = submatrix
matrix.print_matrix()
