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
MAX_TASTE = 1_000_000

def main() -> None:
    # 입력을 처리합니다.
    data = input().strip().splitlines()
    n = int(data[0])  # 수정이가 사탕상자에 손을 댄 횟수
    
    # 세그먼트 트리 초기화
    # 세그먼트 트리에서 각 인덱스는 특정 맛의 사탕 개수를 나타냄
    seg_tree = SegmentTree([0] * (MAX_TASTE + 1), lambda x, y: x + y, 0)
    
    result = []
    
    for i in range(1, n + 1):
        query = list(map(int, data[i].split()))
        
        if query[0] == 1:
            # 사탕 꺼내기: B번째로 맛있는 사탕을 꺼냄
            B = query[1]
            low, high = 1, MAX_TASTE
            
            # 이분 탐색을 통해 B번째로 맛있는 사탕을 찾습니다.
            while low < high:
                mid = (low + high) // 2
                if seg_tree.query(1, mid + 1) >= B:  # mid까지의 사탕 개수가 B 이상이면
                    high = mid  # 더 작은 구간으로 탐색
                else:
                    low = mid + 1  # 더 큰 구간으로 탐색
            
            # 찾은 사탕을 출력하고 해당 사탕을 하나 제거
            result.append(str(low))
            seg_tree.update(low, seg_tree.query(low, low + 1) - 1)
        
        elif query[0] == 2:
            # 사탕 넣기 또는 빼기: 맛이 B인 사탕을 C개 추가 또는 제거
            B, C = query[1], query[2]
            current_count = seg_tree.query(B, B + 1)
            seg_tree.update(B, current_count + C)
    
    # 결과 출력
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()