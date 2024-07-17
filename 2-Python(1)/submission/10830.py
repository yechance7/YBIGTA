from __future__ import annotations
import copy


"""
TODO:
- __setitem__ �����ϱ�
- __pow__ �����ϱ� (__matmul__�� Ȱ���غ��ô�)
- __repr__ �����ϱ�
"""


class Matrix:
    # MOD: ��ⷯ ������ ���ذ� (1000)
    MOD = 1000

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    ## ���� �޼���
    # full: �־��� ������ ä���� ��Ļ���
    @staticmethod
    def full(n: int, shape: tuple[int, int]) -> Matrix:
        return Matrix([[n] * shape[1] for _ in range(shape[0])])
    
    # zeros: ��� ��Ұ� 0�� ����� ����
    @staticmethod
    def zeros(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(0, shape)

    # ones: ��� ��Ұ� 1�� ����� ����
    @staticmethod
    def ones(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(1, shape)

    # eye: ���� ����� ����
    @staticmethod
    def eye(n: int) -> Matrix:
        matrix = Matrix.zeros((n, n))
        for i in range(n):
            matrix[i, i] = 1
        return matrix

    ## �Ӽ� �� ��ƿ��Ƽ �޼���
    # shape: ����� ũ�⸦ ��ȯ
    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.matrix), len(self.matrix[0]))
    # clone: ����� ���� ���纻�� ����
    def clone(self) -> Matrix:
        return Matrix(copy.deepcopy(self.matrix))

    ## �ε��� �޼���
    # __getitem__: Ư�� ��ġ�� ��Ҹ� ������
    def __getitem__(self, key: tuple[int, int]) -> int:
        return self.matrix[key[0]][key[1]]

    # __setitem__: Ư�� ��ġ�� ��Ҹ� ���� -> ��İ��� 1000���Ϸ� �����ǰ�
    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        self.matrix[key[0]][key[1]] = value % self.MOD 

    # __matmul__: �� ����� ���� ó��    
    def __matmul__(self, matrix: Matrix) -> Matrix:
        x, m = self.shape
        m1, y = matrix.shape
        assert m == m1

        result = self.zeros((x, y))

        for i in range(x):
            for j in range(y):
                for k in range(m):
                    result[i, j] += self[i, k] * matrix[k, j]

        return result

    def __pow__(self, n: int) -> Matrix:
        if n == 0: # �������
            return Matrix.eye(self.shape[0])
        elif n == 1: # �ڱ��ڽ�
            return self
        elif n % 2 == 0: # ¦���� ���, ������ �����Ͽ� ��������� ���
            half_pow = self ** (n // 2)
            return half_pow @ half_pow
        else: # Ȧ���� ���, n-1 �ŵ������� ����� �ڱ� �ڽ��� ����
            return self @ (self ** (n - 1))

    def __repr__(self) -> str:
        # �� ���� ���ڿ��� ��ȯ�� �� �ٹٲ� ���ڸ� ����Ͽ� ����
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])


from typing import Callable
import sys


"""
�ƹ��͵� �������� ������!
"""


def main() -> None:
    intify: Callable[[str], list[int]] = lambda l: [*map(int, l.split())]

    #���پ� �о��
    lines: list[str] = sys.stdin.readlines()

    # ����� ũ��(N)�� �ŵ����� Ƚ��(B) �������� ������ ��� ������(matrix)
    N, B = intify(lines[0])
    matrix: list[list[int]] = [*map(intify, lines[1:])]

    
    Matrix.MOD = 1000
    modmat = Matrix(matrix)

    print(modmat ** B)


if __name__ == "__main__":
    main()