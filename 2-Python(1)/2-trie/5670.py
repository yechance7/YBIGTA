from lib import Trie
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
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        new_index = None # 구현하세요!
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