from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""

MOD = 1_000_000_007
T = TypeVar("T")

@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None  # 노드의 값 (예: 문자 또는 숫자)
    children: list[int] = field(default_factory=lambda: [])  # 자식 노드들의 인덱스
    is_end: bool = False  # 이 노드가 문자열의 끝인지 여부


class Trie(list[TrieNode[T]]):
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
            if char not in self[current].children:
                new_node = len(self)
                self[current].children[char] = new_node
                self.append(TrieNode(body=char))
            current = self[current].children[char]

    def is_prefix(self, seq: Iterable[T]) -> bool:
        """
        seq가 현재 트리의 접두사인지 확인합니다.
        """
        current = 0
        for char in seq:
            if char not in self[current].children:
                return False
            current = self[current].children[char]
        return True