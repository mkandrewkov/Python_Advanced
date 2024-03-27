import numpy as np 

def test(Matrix):
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


def test_1():
    from src.matrix_one import Matrix
    test(Matrix)
    # A = np.random.randint(0, 10, (10, 10))
    # B = np.random.randint(0, 10, (10, 10))

    # print('+')
    # print(A + B)

    # print('*')
    # print(A * B)

    # print('@')
    # print(A @ B)

    # A = Matrix(A)
    # B = Matrix(B)

    # (A + B).save_txt('matrix+.txt')
    # (A * B).save_txt('matrix*.txt')
    # (A @ B).save_txt('matrix@.txt')

def test_2():
    from src.matrix_two import Matrix
    test(Matrix)

    # A = np.random.randint(0, 10, (10, 10))
    # B = np.random.randint(0, 10, (10, 10))

    # print('+')
    # print(A + B)

    # print('*')
    # print(A * B)

    # print('@')
    # print(A @ B)

    # A = Matrix(A)
    # B = Matrix(B)

    # (A + B).save_txt('matrix+.txt')
    # (A * B).save_txt('matrix*.txt')
    # (A @ B).save_txt('matrix@.txt')

test_1()
test_2()