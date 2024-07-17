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
- main �����ϱ�

��Ʈ: �� ����¥�� �ڷῡ�� �׳� str�� ���⿡�� �޸𸮰� �Ʊ���...
"""


def main() -> None:
    trie = Trie()
    input = sys.stdin.read().split()

    for word in input:
        trie.push(word)

    # �ڽ��� ������ ��� ���ϴ� ������� Ǯ�� �ȴ�. 0�� �����Ѵ�.
    MOD = 1_000_000_007
    product = 1
    for node in trie:
        num_children = len(node.children)
        if num_children > 0:
            product = (product * num_children) % MOD

    print(product)
    


if __name__ == "__main__":
    main()