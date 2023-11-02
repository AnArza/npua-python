from matrix import Matrix


m1 = Matrix(2, 3)
print('Matrix1:')
print(m1)

m2 = Matrix(3, 2)
print('Matrix2:')
print(m2)

m3 = m1 * m2
print('Multiplied Matrices:')
print(m3)

m4 = Matrix(2, 3)
print('Matrix4:')
print(m4)

m5 = m1 + m4
print("Added Matrices (1 and 4):")
print(m5)

m6 = m1 - m4
print("Subtracted Matrices (1 and 4):")
print(m6)
