"""
Задача является продолжением задачи 3.1
Придумать и реализовать простейшую хэш-функцию (дать краткое текстовое описание в комментариях в коде) для матрицы  в методе __hash__ (вынести в примесь).
Ограничение на хэш-функцию - она должна быть не константой (не возвращать всегда одно число)
Настроить кэширование произведения матриц по этой хэш-функции
Найти коллизию в хэш-функции (если поиск производится кодом, то код также нужно выложить)
"""
import numpy as np
from .matrix_one import Matrix

class MatrixHashMixin:

    def __hash__(self):
        # Простейшая хэш-функция для матрицы - сумма всех элементов матрицы
        return hash(sum(map(sum, self.data)))


class MatrixWithHash(Matrix, MatrixHashMixin):

    def __init__(self, data):
        super().__init__(data)


