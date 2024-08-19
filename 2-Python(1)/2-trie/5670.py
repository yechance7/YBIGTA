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