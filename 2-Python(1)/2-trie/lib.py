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
    MOD = 1000000007  # 모듈러 연산을 위한 상수

    def __init__(self) -> None:
        # Trie는 기본적으로 리스트의 형태이며, 루트 노드를 초기화하면서 시작함
        super().__init__()
        self.append(TrieNode(body=None))  # 루트 노드 추가

    def push(self, seq: Iterable[T]) -> None:
        """
        트라이에 시퀀스를 삽입하는 메서드
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)
        """
        current = 0  # 루트 노드에서 시작
        for char in seq:
            found = False  # 현재 노드의 자식 중에 해당 문자가 있는지 확인하는 플래그
            for child in self[current].children:  # 현재 노드의 자식들을 순회
                if self[child].body == char:  # 이미 존재하는 문자라면
                    current = child  # 해당 자식으로 이동
                    found = True  # 문자를 찾았음을 표시
                    break  # 더 이상 찾을 필요 없음
            if not found:  # 자식 중에 문자가 없으면
                new_node = TrieNode(body=char)  # 새로운 노드를 생성
                self.append(new_node)  # 트라이에 새 노드를 추가
                self[current].children.append(len(self) - 1)  # 현재 노드의 자식으로 추가된 노드의 인덱스를 추가
                current = len(self) - 1  # 현재 노드를 새로 추가된 노드로 변경
        self[current].is_end = True  # 마지막 노드를 시퀀스의 끝으로 표시

    def count_orderings(self, node_index: int = 0) -> int:
        """
        주어진 노드에서부터 가능한 시퀀스의 순서 수를 계산하는 메서드
        node_index: 시작 노드의 인덱스 (기본값은 루트 노드인 0)
        """
        node = self[node_index]
        if not node.children:  # 자식이 없으면 리프 노드이므로 순서 수는 1
            return 1

        num_children = len(node.children)  # 자식 노드 수
        subtree_orderings = 1  # 서브트리 순서 수를 곱해가며 계산

        for child_idx in node.children:  # 각 자식에 대해 순서 수를 재귀적으로 계산
            subtree_orderings *= self.count_orderings(child_idx)
            subtree_orderings %= self.MOD  # 모듈러 연산 적용

        return (self.factorial(num_children) * subtree_orderings) % self.MOD  # 자식들의 순서와 조합하여 전체 순서 수 계산

    def factorial(self, n: int) -> int:
        """
        주어진 n에 대한 팩토리얼을 계산하는 메서드
        """
        result = 1
        for i in range(2, n + 1):
            result *= i  # 팩토리얼 계산
        return result  # 결과 반환
    
    def contains(self, seq: Iterable[T]) -> int:
        """
        주어진 시퀀스가 트라이 내에 포함된 횟수를 계산하는 메서드
        seq: 시퀀스
        """
        count = 0  # 시퀀스 포함 횟수 카운터
        current = 0  # 루트 노드에서 시작
        for c in seq:  # 시퀀스의 각 문자에 대해
            for child in self[current].children:  # 현재 노드의 자식들을 순회
                if self[child].body == c:  # 문자가 존재하면
                    current = child  # 해당 자식으로 이동
                    break  # 다음 문자로 넘어감
            if len(self[current].children) > 1 or self[current].is_end:  # 자식이 둘 이상이거나 문자열의 끝이라면
                count += 1  # 시퀀스 포함 횟수 증가
        return count  # 포함된 횟수 반환
