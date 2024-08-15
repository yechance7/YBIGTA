from __future__ import annotations
import copy


"""
TODO:
- __setitem__ 구현하기
- __pow__ 구현하기 (__matmul__을 활용해봅시다)
- __repr__ 구현하기
"""


class Matrix:
    MOD = 1000

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    @staticmethod
    def full(n: int, shape: tuple[int, int]) -> Matrix:
        """모든 원소가 n인 행렬을 생성"""
        return Matrix([[n] * shape[1] for _ in range(shape[0])])

    @staticmethod
    def zeros(shape: tuple[int, int]) -> Matrix:
        """모든 원소가 0인 행렬을 생성"""
        return Matrix.full(0, shape)

    @staticmethod
    def ones(shape: tuple[int, int]) -> Matrix:
        """모든 원소가 1인 행렬을 생성"""
        return Matrix.full(1, shape)

    @staticmethod
    def eye(n: int) -> Matrix:
        """단위 행렬 생성"""
        matrix = Matrix.zeros((n, n))
        for i in range(n):
            matrix[i, i] = 1
        return matrix

    @property
    def shape(self) -> tuple[int, int]:
        """행렬의 형태를 반환"""
        return (len(self.matrix), len(self.matrix[0]))

    def clone(self) -> Matrix:
        """행렬의 복사본을 생성"""
        return Matrix(copy.deepcopy(self.matrix))

    def __getitem__(self, key: tuple[int, int]) -> int:
        """행렬의 특정 원소에 접근"""
        return self.matrix[key[0]][key[1]]

    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        """행렬의 특정 원소에 값을 설정"""
        self.matrix[key[0]][key[1]] = value % Matrix.MOD

    def __matmul__(self, matrix: Matrix) -> Matrix:
        """행렬의 곱셈을 수행"""
        x, m = self.shape
        m1, y = matrix.shape
        assert m == m1  # 행렬의 곱셈이 가능하려면 두 행렬의 열 수가 같아야 한다

        result = self.zeros((x, y))

        for i in range(x):
            for j in range(y):
                for k in range(m):
                    result[i, j] += self[i, k] * matrix[k, j] # 모듈로 연산을 통해 결과를 1000으로 나눈 나머지로 유지

        return result

    def __pow__(self, n: int) -> Matrix:
        """행렬의 n제곱을 수행"""
        result = Matrix.eye(self.shape[0])  # 단위 행렬로 초기화
        base = self.clone()

        while n > 0:
            if n % 2 == 1:
                result = result @ base
            base = base @ base
            n //= 2

        return result

    def __repr__(self) -> str:
        """행렬을 문자열로 변환하여 출력"""
        return '\n'.join(' '.join(str(self[i, j]) for j in range(self.shape[1])) for i in range(self.shape[0]))