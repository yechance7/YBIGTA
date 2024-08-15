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
        # 현재 노드에서 자식이 2개 이상이거나, 현재 노드 자체가 단어의 끝이라면 버튼을 눌러야 한다
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        # 현재 글자에 해당하는 자식 노드를 찾음
        new_index = None # 구현하세요!
        for child_index in trie[pointer].children:
            if trie[child_index].body == element:
                new_index = child_index
                break
        
        # 새 노드로 포인터 이동
        pointer = new_index

    # 마지막 글자에 대해 체크 (루트 노드가 자식이 1개일 때 자동으로 입력된 경우 체크)
    return cnt + int(len(trie[0].children) == 1)


def main() -> None:
    input = sys.stdin.read
    data = input().strip().splitlines()

    idx = 0
    results = []

    while idx < len(data):
        N = int(data[idx])  # 단어의 개수
        idx += 1
        words = data[index:index+N]
        index += N

        # Trie에 단어들을 삽입
        trie = Trie[str]()
        for word in words:
            trie.push(word)
        

        # 각 단어에 대해 버튼 입력 횟수 계산
        total_presses = 0
        for word in words:
            total_presses += count(trie, word)
        
        # 평균 버튼 입력 횟수 계산 및 저장
        average_presses = total_presses / N
        results.append(f"{average_presses:.2f}")

    # 결과 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()