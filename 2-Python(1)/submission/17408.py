from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree 구현하기
"""


T = TypeVar("T")
U = TypeVar("U")

class SegmentTree(Generic[T, U]):
    """
    세그먼트 트리(Segment Tree) 클래스입니다.
    주어진 배열에 대해 특정 범위의 값을 빠르게 계산하기 위해 사용됩니다.
    예를 들어, 구간 합, 최소값, 최대값 등을 계산할 수 있습니다.
    """

    def __init__(self, data: list[T], func: Callable[[U, U], U], default: U):
        """
        세그먼트 트리의 초기화 메서드입니다.

        :param data: 원본 데이터 배열입니다.
        :param func: 구간에 대해 계산할 함수입니다. 예: 합계, 최소값, 최대값 등.
        :param default: 기본 값으로, 트리의 리프 노드에 해당하는 값이 없습니다.
        """
        self.n = len(data)  # 입력 데이터의 크기
        self.func = func  # 트리의 각 노드에서 사용할 함수
        self.default = default  # 트리의 기본 값
        self.tree = [default] * (2 * self.n)  # 세그먼트 트리 배열 초기화

        # 입력 데이터를 세그먼트 트리의 리프 노드에 채웁니다.
        for i in range(self.n):
            self.tree[self.n + i] = data[i]

        # 리프 노드를 바탕으로 내부 노드를 계산합니다.
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index: int, value: T) -> None:
        """
        특정 인덱스의 값을 업데이트하고 세그먼트 트리를 갱신합니다.

        :param index: 업데이트할 데이터의 인덱스 (0-based index).
        :param value: 새롭게 설정할 값.
        """
        # 리프 노드에서 값을 업데이트합니다.
        pos = self.n + index
        self.tree[pos] = value

        # 트리의 상위 노드들을 업데이트합니다.
        pos //= 2
        while pos > 0:
            self.tree[pos] = self.func(self.tree[2 * pos], self.tree[2 * pos + 1])
            pos //= 2

    def query(self, left: int, right: int) -> U:
        """
        주어진 범위 [left, right) 내의 구간 값을 계산합니다.

        :param left: 구간의 시작 인덱스 (포함, 0-based index).
        :param right: 구간의 끝 인덱스 (미포함, 0-based index).
        :return: 구간 [left, right) 에 대한 계산 결과.
        """
        result = self.default

        # 인덱스를 리프 노드에 맞춥니다.
        left += self.n
        right += self.n

        while left < right:
            # left가 홀수라면, 현재 노드를 결과에 포함시키고, 다음 구간으로 넘어갑니다.
            if left % 2 == 1:
                result = self.func(result, self.tree[left])
                left += 1
            # right가 홀수라면, 현재 노드를 결과에 포함시키고, 다음 구간으로 넘어갑니다.
            if right % 2 == 1:
                right -= 1
                result = self.func(result, self.tree[right])

            # 상위 노드로 이동합니다.
            left //= 2
            right //= 2

        return result



import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


class Pair(tuple[int, int]):
    """
    힌트: 2243, 3653에서 int에 대한 세그먼트 트리를 만들었다면 여기서는 Pair에 대한 세그먼트 트리를 만들 수 있을지도...?
    """
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
        """
        기본값
        이게 왜 필요할까...?

        기본값을 반환합니다. 초기화 시에 사용됩니다.
        """
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
        """
        원본 수열의 값을 대응되는 Pair 값으로 변환하는 연산
        이게 왜 필요할까...?

        주어진 값을 Pair 형식으로 변환합니다. 두 번째 값은 항상 0입니다.
        """
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: Pair, b: Pair) -> 'Pair':
        """
        두 Pair를 하나의 Pair로 합치는 연산
        이게 왜 필요할까...?

        두 Pair 객체를 병합하여 가장 큰 두 값을 가진 Pair를 반환합니다.
        """
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]


def main() -> None:
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    
    # 수열의 크기 N 읽기
    N = int(data[index])
    index += 1
    
    # 수열 A 읽기
    A = list(map(int, data[index:index + N]))
    index += N
    
    # 쿼리의 개수 M 읽기
    M = int(data[index])
    index += 1
    
    # 쿼리 읽기
    queries = data[index:index + 3 * M]
    
    # SegmentTree를 초기화
    seg_tree = SegmentTree([Pair(x, 0) for x in A], 
                           operation=Pair.f_merge, 
                           default=Pair.default())
    
    results = []
    
    # 쿼리 처리
    for i in range(M):
        q_type = int(queries[3 * i])
        if q_type == 1:
            # 1 i v: Ai를 v로 바꾼다.
            i = int(queries[3 * i + 1]) - 1
            v = int(queries[3 * i + 2])
            seg_tree.update(i, Pair.f_conv(v))
        elif q_type == 2:
            # 2 l r: l ≤ i < j ≤ r을 만족하는 모든 Ai + Aj 중에서 최댓값을 출력한다.
            l = int(queries[3 * i + 1]) - 1
            r = int(queries[3 * i + 2]) - 1
            result = seg_tree.query(l, r).sum()
            results.append(result)
    
    # 결과 출력
    sys.stdout.write('\n'.join(map(str, results)) + '\n')


if __name__ == "__main__":
    main()
