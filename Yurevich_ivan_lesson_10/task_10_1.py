from typing import List
from itertools import zip_longest


class Matrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def __str__(self):
        result = '\n'.join(['\t'.join([f'{el}' for el in row]) for row in self.matrix])
        return f'{result}\n'

    def __add__(self, other):
        return Matrix([[(x + y) for x, y in zip_longest(i, j, fillvalue=0)] for i, j in zip_longest(self.matrix, other.matrix, fillvalue=[])])



if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """