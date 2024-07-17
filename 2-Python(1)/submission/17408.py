from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree �����ϱ�
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    def __init__(self, data: List[T], func: Callable[[U, U], U], default: U):
        self.n = len(data)
        self.func = func
        self.default = default
        self.tree = [default] * (2 * self.n)
        self.build(data)

    def build(self, data: List[T]):
        # Insert leaf nodes in tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, index: int, value: T):
        # Update leaf node
        pos = index + self.n
        self.tree[pos] = value
        # Update internal nodes
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.func(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, left: int, right: int) -> U:
        # Query range [left, right)
        result = self.default
        left += self.n
        right += self.n
        while left < right:
            if left % 2:
                result = self.func(result, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                result = self.func(result, self.tree[right])
            left //= 2
            right //= 2
        return result


import sys


"""
TODO:
- �ϴ� SegmentTree���� �����ϱ�
- main �����ϱ�
"""


class Pair(tuple[int, int]):
    """
    ��Ʈ: 2243, 3653���� int�� ���� ���׸�Ʈ Ʈ���� ������ٸ� ���⼭�� Pair�� ���� ���׸�Ʈ Ʈ���� ���� �� ��������...?
    """
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
        """
        �⺻��
        �̰� �� �ʿ��ұ�...?
        """
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
        """
        ���� ������ ���� �����Ǵ� Pair ������ ��ȯ�ϴ� ����
        �̰� �� �ʿ��ұ�...?
        """
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: Pair, b: Pair) -> 'Pair':
        """
        �� Pair�� �ϳ��� Pair�� ��ġ�� ����
        �̰� �� �ʿ��ұ�...?
        """
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]


def main() -> None:
    # �����ϼ���!
    pass


if __name__ == "__main__":
    main()