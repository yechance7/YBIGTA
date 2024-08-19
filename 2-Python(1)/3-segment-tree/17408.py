from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


class Pair(tuple[int, int]):
    """
    힌트: 2243, 3653에서 int에 대한 세그먼트 트리를 만들었다면 여기서는 Pair에 대한 세그먼트 트리를 만들 수 있을지도...?
    """
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
        """
        기본값
        이게 왜 필요할까...?

        기본값을 반환합니다. 초기화 시에 사용됩니다.
        """
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
        """
        원본 수열의 값을 대응되는 Pair 값으로 변환하는 연산
        이게 왜 필요할까...?

        주어진 값을 Pair 형식으로 변환합니다. 두 번째 값은 항상 0입니다.
        """
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: 'Pair', b: 'Pair') -> 'Pair':
        """
        두 Pair를 하나의 Pair로 합치는 연산
        이게 왜 필요할까...?

        두 Pair 객체를 병합하여 가장 큰 두 값을 가진 Pair를 반환합니다.
        """
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]


def main() -> None:
    input = sys.stdin.read().strip()

    data = input.split()
    
    index = 0
    
    # 수열의 크기 N 읽기
    N = int(data[index])
    index += 1
    
    # 수열 A 읽기
    A = list(map(int, data[index:index + N]))
    index += N
    
    # 쿼리의 개수 M 읽기
    M = int(data[index])
    index += 1
    

    # SegmentTree를 초기화
    tree: SegmentTree[Pair, int] = SegmentTree(N, Pair.f_merge, Pair.default())

    for i in range(N):
        tree.update_17408(i, Pair.f_conv(A[i]))
    
    results = []
    
    # 쿼리 처리
    for i in range(M):
        q_type = int(data[index])
        if q_type == 1:
            # 1 i v: Ai를 v로 바꾼다.
            i = int(data[index+1]) - 1
            v = int(data[index+2])
            tree.update_17408(i, Pair.f_conv(v))
            index += 3
        elif q_type == 2:
            # 2 left right: left ≤ i < j ≤ right 만족하는 모든 Ai + Aj 중에서 최댓값을 출력한다.
            left = int(data[index+1]) - 1
            right = int(data[index+2])
            result = str(tree.query(left, right).sum())
            results.append(result)
            index += 3
    
    # 결과 출력
    print("\n".join(results))


if __name__ == "__main__":
    main()
