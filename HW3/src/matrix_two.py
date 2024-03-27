"""
Используя примеси numpy, сделать класс, который будет уметь выполнять все стандартные арифметические операции.
Также добавить через примеси: запись объекта в файл, красивое отображение в консоли (__str__), getter-ы и setter-ы для полей класса
В самих классах должно быть минимальное количество методов

"""
import numpy as np

class FileIOMixin:
    def save_txt(self, filename):
        with open('artifacts/3.2/'+filename, 'w+') as writer:
            writer.write(str(self))


class DisplayMixin:
    def __str__(self):
        return '\n'.join([str(arr) for arr in self.value])
    

class ArithmeticOperationsMixin:
    def __add__(self, other):
        return self.__class__(self.value + other.value)

    def __sub__(self, other):
        return self.__class__(self.value - other.value)

    def __mul__(self, other):
        return self.__class__(self.value * other.value)

    def __truediv__(self, other):
        return self.__class__(self.value / other.value)
    
    def __matmul__(self, other):
        return self.__class__(self.value @ other.value)


class Matrix(ArithmeticOperationsMixin, DisplayMixin, FileIOMixin):
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = np.array(value)
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, matrix):
        row_size = len(matrix[0])
        try:
            for arr in matrix:
                assert len(arr) == row_size
        except:
            raise ValueError(f'Строки имеют разную длину')
        self._value = np.array(matrix)
