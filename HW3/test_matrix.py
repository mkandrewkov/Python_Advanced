import numpy as np 

from src.matrix import Matrix

np.random.seed(0)


A = np.random.randint(0, 10, (10, 10))
B = np.random.randint(0, 10, (10, 10))


print('+')
print(A + B)

print('*')
print(A * B)

print('@')
print(A @ B)

A = Matrix(A)
B = Matrix(B)

(A + B).save_txt('matrix+.txt')
(A * B).save_txt('matrix*.txt')
(A @ B).save_txt('matrix@.txt')
