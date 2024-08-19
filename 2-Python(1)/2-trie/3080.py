from lib import Trie
import sys


"""
TODO:
- 일단 Trie부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


def main() -> None:
    MOD = 1_000_000_007
    
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    names = data[1:]
    
    # Trie 생성
    trie = Trie()
    for name in names:
        trie.push(name)
    
    # 사전 순으로 정렬
    names.sort()
    
    # DP 배열 초기화
    dp = [0] * N
    dp[0] = 1
    
    # DP 계산
    for i in range(1, N):
        dp[i] = 1
        for j in range(i):
            if trie.is_prefix(names[j]):
                dp[i] = (dp[i] + dp[j]) % MOD
    
    # 결과 출력
    result = sum(dp) % MOD
    print(result)


if __name__ == "__main__":
    main()