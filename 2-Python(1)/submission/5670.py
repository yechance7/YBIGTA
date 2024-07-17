from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push �����ϱ�
- (�ʿ��� ���) Trie�� �߰� method �����ϱ�
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False
# body: ������, children: �ڽ� ���, is_end: ������ ����������
# self�� ���� 3���� ������ �ϳ��� ����Ʈ

class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T�� �� (list[int]�� ���� �ְ� str�� ���� �ְ� ���...)

        action: trie�� seq�� �����ϱ�
        """
        current_node_index = 0  # ��Ʈ ����� �ε���

        # �ش� �ܾ �ҷ��´� (seq)
        for element in seq:
            # ������� ����
            found_in_child = False
            # �ڽĳ�带 �ҷ��´�
            for child_index in self[current_node_index].children:
                if self[child_index].body == element:
                    # ��Ҹ� ���� �ڽ� ��尡 ������ �� ���� �̵�
                    current_node_index = child_index
                    found_in_child = True
                    break
            
            if not found_in_child:
                # ��Ҹ� ���� �ڽ� ��尡 ������ ���ο� ��� �߰�
                new_node = TrieNode(body=element)
                self.append(new_node)
                new_node_index = len(self) - 1
                self[current_node_index].children.append(new_node_index)
                current_node_index = new_node_index
        
        # �������� ���� ǥ��
        self[current_node_index].is_end = True




import sys


"""
TODO:
- �ϴ� Trie���� �����ϱ�
- count �����ϱ�
- main �����ϱ�
"""


def count(trie: Trie, query_seq: str) -> int:
    """
    trie - �̸� �״�� trie
    query_seq - �ܾ� ("hello", "goodbye", "structures" ��)

    returns: query_seq�� �ܾ �Է��ϱ� ���� ��ư�� ������ �ϴ� Ƚ��
    """
    pointer = 0
    cnt = 0

    for element in query_seq:
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        new_index = None # �����ϼ���!
        for child in trie[pointer].children:
            if child.char == element:
                new_index = child.index
                break
        
        if new_index is None:
            raise ValueError(f"Character {element} not found in Trie")
        
        pointer = new_index

    return cnt + int(len(trie[0].children) == 1)


def main() -> None:
    input = sys.stdin.read
    data = input().strip().split('\n')

    i = 0
    while i < len(data):
        n = int(data[i].strip())
        i += 1

        words = []
        for _ in range(n):
            words.append(data[i].strip())
            i += 1
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        total_presses = sum(trie.count_presses(word) for word in words)
        avg_presses = total_presses / len(words)
        
        print(f"{avg_presses:.2f}")


if __name__ == "__main__":
    main()