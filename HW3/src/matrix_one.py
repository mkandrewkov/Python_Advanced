"""
Нужно реализовать небольшую библиотеку для работы с матрицами
3.1
Сделать класс матрицы, в котором определить операции сложения и умножения (матричного и покомпонентного) 
через перегрузку операторов +, *, @ (как в numpy). Вызывать исключения, если матрицы на входе некорректной размерности (ValueError)
Сгенерировать две матрицы через np.random.randint(0, 10, (10, 10)) c seed-ом 0 и над ними провести все три операции. 
Записать результаты в текстовые файлы, названные matrix+.txt, matrix*.txt, matrix@.txt, соответственно. Это будет артефактом задачи.
"""
import typing as tp

class Matrix:
    def __init__(self, data: tp.List[tp.List[float]]):
        self.data = data

    def save_txt(self, filename):
        with open('artifacts/3.1/'+filename, 'w+') as writer:
            writer.write(str(self))

    def __matmul__(self, other):
        """Произведение матриц"""
        try:
            assert self.shape[1] == other.shape[0]
        except:
            raise ValueError(f'Число столбцов левой матрицы {self.shape[1]} не равно числу строк правой матрицыи {other.shape[0]}')
        
        result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*other.data)] for X_row in self.data]
        return Matrix(result)

    def __add__(self, other):
        """Сложение матриц"""
        try:
            assert self.shape == other.shape
        except:
            raise ValueError(f'Матрицы имеют разные размерности {self.shape} и {other.shape}')
        
        result = []
        for arr_a, arr_b in zip(self.data, other.data):
            sum_arr = []
            for a, b in zip(arr_a, arr_b):
                sum_arr.append(a+b)
            result.append(sum_arr)
        return Matrix(result)

    def __mul__(self, other):
        
        """Поэлементное умножение матриц"""
        try:
            assert self.shape == other.shape
        except:
            raise ValueError(f'Матрицы имеют разные размерности {self.shape} и {other.shape}')
        
        result = []
        for arr_a, arr_b in zip(self.data, other.data):
            mul_arr = []
            for a, b in zip(arr_a, arr_b):
                mul_arr.append(a*b)
            result.append(mul_arr)
        return Matrix(result)

    def __str__(self,):
        return '\n'.join([str(arr) for arr in self.data])

    @property
    def shape(self):
        return len(self.data), len(self.data[0])
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, matrix):
        row_size = len(matrix[0])
        try:
            for arr in matrix:
                assert len(arr) == row_size
        except:
            raise ValueError(f'Строки имеют разную длину')
        self._data = matrix


    

