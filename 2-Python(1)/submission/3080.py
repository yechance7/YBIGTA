from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""

T = TypeVar("T")

@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None  # 노드의 값 (예: 문자 또는 숫자)
    children: list[int] = field(default_factory=lambda: [])  # 자식 노드들의 인덱스
    is_end: bool = False  # 이 노드가 문자열의 끝인지 여부


class Trie(list[TrieNode[T]]):
    MOD = 1000000007

    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))  # 루트 노드 추가

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)
        
        트라이에 시퀀스를 삽입하는 메서드
        """
        current = 0
        for char in seq:
            found = False
            for child in self[current].children:
                if self[child].body == char:
                    current = child
                    found = True
                    break
            if not found:
                new_node = TrieNode(body=char)
                self.append(new_node)
                self[current].children.append(len(self) - 1)
                current = len(self) - 1
        self[current].is_end = True

    def count_orderings(self, node_index: int = 0) -> int:
        node = self[node_index]
        if not node.children:
            return 1

        num_children = len(node.children)
        subtree_orderings = 1

        for child_idx in node.children:
            subtree_orderings *= self.count_orderings(child_idx)
            subtree_orderings %= self.MOD

        return (self.factorial(num_children) * subtree_orderings) % self.MOD

    def factorial(self, n: int) -> int:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def contains(self, seq: Iterable[T]) -> int:
        count = 0
        current = 0
        for c in seq:
            for child in self[current].children:
                if self[child].body == c:
                    current = child
                    break
            if len(self[current].children) > 1 or self[current].is_end:
                count += 1
        return count


import sys


"""
TODO:
- 일단 Trie부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


MOD = 1_000_000_007

def main() -> None:
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    names = data[1:]
    
    # Trie 생성
    trie = Trie()
    for name in names:
        trie.push(name)
    
    # 사전 순으로 정렬
    names.sort()
    
    # DP 배열 초기화
    dp = [0] * N
    dp[0] = 1
    
    # DP 계산
    for i in range(1, N):
        dp[i] = 1
        for j in range(i):
            if trie.is_prefix(names[j]):
                dp[i] = (dp[i] + dp[j]) % MOD
    
    # 결과 출력
    result = sum(dp) % MOD
    print(result)


if __name__ == "__main__":
    main()