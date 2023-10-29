from matrix_operations import generate_random_matrix, get_column_sum, get_row_average


matrix = generate_random_matrix(5, 6)

for row in matrix:
    print(row)
print(f'The sum of the elements in the 5th column is {get_column_sum(matrix, 4)}')
print(f'The average value of the 4th row is {get_row_average(matrix, 3)}')
