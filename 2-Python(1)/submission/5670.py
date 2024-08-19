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
- count 구현하기
- main 구현하기
"""


def count(trie: Trie, query_seq: str) -> int:
    """
    trie - 이름 그대로 trie
    query_seq - 단어 ("hello", "goodbye", "structures" 등)

    returns: query_seq의 단어를 입력하기 위해 버튼을 눌러야 하는 횟수
    """
    pointer = 0
    cnt = 0

    for element in query_seq:
        # 현재 글자에 해당하는 자식 노드를 찾음
        for child_index in trie[pointer].children:
            if trie[child_index].body == element:
                pointer = child_index
                break
        
        # 현재 노드에서 자식이 2개 이상이거나, 현재 노드 자체가 단어의 끝이라면 버튼을 눌러야 한다
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1
    
    return cnt 


def main() -> None:
    while True:
        try:
            N = int(sys.stdin.readline())
        except:
            break
    
        trie = Trie[str]()
        words = []
        for _ in range(N):
            word = sys.stdin.readline().rstrip()
            trie.push(word)
            words.append(word)

        total_presses = sum(count(trie, word) for word in words)
        print(f"{total_presses / N:.2f}")

if __name__ == "__main__":
    main()