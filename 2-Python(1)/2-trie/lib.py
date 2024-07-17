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
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False
# body: 실제값, children: 자식 노드, is_end: 마지막 값인지여부
# self는 위에 3개로 구성된 하나의 리스트

class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기
        """
        current_node_index = 0  # 루트 노드의 인덱스

        # 해당 단어를 불러온다 (seq)
        for element in seq:
            # 디폴드는 없다
            found_in_child = False
            # 자식노드를 불러온다
            for child_index in self[current_node_index].children:
                if self[child_index].body == element:
                    # 요소를 가진 자식 노드가 있으면 그 노드로 이동
                    current_node_index = child_index
                    found_in_child = True
                    break
            
            if not found_in_child:
                # 요소를 가진 자식 노드가 없으면 새로운 노드 추가
                new_node = TrieNode(body=element)
                self.append(new_node)
                new_node_index = len(self) - 1
                self[current_node_index].children.append(new_node_index)
                current_node_index = new_node_index
        
        # 시퀀스의 끝을 표시
        self[current_node_index].is_end = True

