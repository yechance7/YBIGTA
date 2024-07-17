from lib import Matrix
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