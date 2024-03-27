from src.matrix_three import MatrixWithHash


# Пример использования
A = MatrixWithHash([[1, 2], [3, 4]])
B = MatrixWithHash([[5, 5], [5, 5]])
D = MatrixWithHash([[5, 5], [5, 5]])
C = MatrixWithHash([[3, 4], [1, 2]])
path = 'artifacts/3.3/'
A.save_txt(filename='A.txt', path=path)
B.save_txt(filename='B.txt', path=path)
C.save_txt(filename='C.txt', path=path)
D.save_txt(filename='D.txt', path=path)
(A @ B).save_txt(filename='AB.txt', path=path)
(C @ D).save_txt(filename='CD.txt', path=path)

with open(path+'hash.txt', 'w+') as writer:
    writer.write(f"hash AB: {str(hash(A @ B))}, hash CD: {str(hash(C @ D))}")

print((hash(A) == hash(C)), (A != C), (B != D), (A @ B != C @ D))
print(hash(A), hash(B), hash(C), hash(D), hash(A * B), hash(A + B), hash(A @ B))

"""
Артефакт - 7 файлов.
A.txt, B.txt, C.txt, D.txt - матрицы, такие, что
(hash(A) == hash(C)) and (A != C) and (B == D) and (A @ B != C @ D)
AB.txt - результат произведения A @ B
CD.txt - настоящий результат произведения C @ D
hash.txt - хэш матриц AB и CD
"""

