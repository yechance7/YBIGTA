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

    def __init__(self, n: int, func: Callable[[T,T], T], T = TypeVar("T", bound=int)):
        """
        세그먼트 트리의 초기화 메서드입니다.

        :param data: 원본 데이터 배열입니다.
        :param func: 구간에 대해 계산할 함수입니다. 예: 합계, 최소값, 최대값 등.
        :param default: 기본 값으로, 트리의 리프 노드에 해당하는 값이 없습니다.
        """
        self.n = n
        self.func = func  # 트리의 각 노드에서 사용할 함수
        self.default = T  # 트리의 기본 값
        self.tree = [T] * (2 * n)  # 세그먼트 트리 배열 초기화


    def update(self, index: int, value: T):
        """
        특정 인덱스의 값을 업데이트하고 세그먼트 트리를 갱신합니다.

        :param index: 업데이트할 데이터의 인덱스 (0-based index).
        :param value: 새롭게 설정할 값.
        """
        # 리프 노드에서 값을 업데이트합니다.
        index += self.n
        self.tree[index] += value

        # 트리의 상위 노드들을 업데이트합니다
        while index > 1:
            index //= 2
            self.tree[index] = self.func(self.tree[2 * index], self.tree[2 * index + 1])
    
    def find_kth(self, k: int) -> int:
        index = 1
        while index < self.n:
            if self.tree[index * 2] >= k:
                index = index * 2
            else:
                k -= self.tree[index * 2]
                index = index * 2 + 1
        return index - self.n
    
    def query(self, left: int, right: int) -> T:
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
    
    def update_17408(self, index: int, value: T):
        """
        특정 인덱스의 값을 업데이트하고 세그먼트 트리를 갱신합니다.

        :param index: 업데이트할 데이터의 인덱스 (0-based index).
        :param value: 새롭게 설정할 값.
        """
        # 리프 노드에서 값을 업데이트합니다.
        index += self.n
        self.tree[index] = value

        # 트리의 상위 노드들을 업데이트합니다
        while index > 1:
            index //= 2
            self.tree[index] = self.func(self.tree[2 * index], self.tree[2 * index + 1])
    
