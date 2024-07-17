from __future__ import annotations
import copy


"""
TODO:
- __setitem__ 구현하기
- __pow__ 구현하기 (__matmul__을 활용해봅시다)
- __repr__ 구현하기
"""


class Matrix:
    # MOD: 모듈러 연산의 기준값 (1000)
    MOD = 1000

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    ## 정적 메서드
    # full: 주어진 값으로 채워진 행렬생성
    @staticmethod
    def full(n: int, shape: tuple[int, int]) -> Matrix:
        return Matrix([[n] * shape[1] for _ in range(shape[0])])
    
    # zeros: 모든 요소가 0인 행렬을 생성
    @staticmethod
    def zeros(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(0, shape)

    # ones: 모든 요소가 1인 행렬을 생성
    @staticmethod
    def ones(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(1, shape)

    # eye: 단위 행렬을 생성
    @staticmethod
    def eye(n: int) -> Matrix:
        matrix = Matrix.zeros((n, n))
        for i in range(n):
            matrix[i, i] = 1
        return matrix

    ## 속성 및 유틸리티 메서드
    # shape: 행렬의 크기를 반환
    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.matrix), len(self.matrix[0]))
    # clone: 행렬의 깊은 복사본을 만듭
    def clone(self) -> Matrix:
        return Matrix(copy.deepcopy(self.matrix))

    ## 인덱싱 메서드
    # __getitem__: 특정 위치의 요소를 가져옴
    def __getitem__(self, key: tuple[int, int]) -> int:
        return self.matrix[key[0]][key[1]]

    # __setitem__: 특정 위치의 요소를 설정 -> 행렬값이 1000이하로 유지되게
    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        self.matrix[key[0]][key[1]] = value % self.MOD 

    # __matmul__: 두 행렬의 곱셈 처리    
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
        if n == 0: # 단위행렬
            return Matrix.eye(self.shape[0])
        elif n == 1: # 자기자신
            return self
        elif n % 2 == 0: # 짝수일 경우, 반으로 분할하여 재귀적으로 계산
            half_pow = self ** (n // 2)
            return half_pow @ half_pow
        else: # 홀수일 경우, n-1 거듭제곱한 결과에 자기 자신을 곱함
            return self @ (self ** (n - 1))

    def __repr__(self) -> str:
        # 각 행을 문자열로 변환한 후 줄바꿈 문자를 사용하여 연결
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])


from typing import Callable
import sys


"""
아무것도 수정하지 마세요!
"""


def main() -> None:
    intify: Callable[[str], list[int]] = lambda l: [*map(int, l.split())]

    #한줄씩 읽어옴
    lines: list[str] = sys.stdin.readlines()

    # 행렬의 크기(N)와 거듭제곱 횟수(B) 가져오고 나머지 행렬 가져옴(matrix)
    N, B = intify(lines[0])
    matrix: list[list[int]] = [*map(intify, lines[1:])]

    
    Matrix.MOD = 1000
    modmat = Matrix(matrix)

    print(modmat ** B)


if __name__ == "__main__":
    main()