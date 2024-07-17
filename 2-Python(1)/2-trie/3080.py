from lib import Trie
import sys


"""
TODO:
- 일단 Trie부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


def main() -> None:
    trie = Trie()
    input = sys.stdin.read().split()

    for word in input:
        trie.push(word)

    # 자식의 갯수를 모두 곱하는 방법으로 풀면 된다. 0은 제외한다.
    MOD = 1_000_000_007
    product = 1
    for node in trie:
        num_children = len(node.children)
        if num_children > 0:
            product = (product * num_children) % MOD

    print(product)
    


if __name__ == "__main__":
    main()