from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""
MAX_TASTE = 1_000_000

def main() -> None:
    # 입력을 처리합니다.
    data = input().strip().splitlines()
    n = int(data[0])  # 수정이가 사탕상자에 손을 댄 횟수
    
    # 세그먼트 트리 초기화
    # 세그먼트 트리에서 각 인덱스는 특정 맛의 사탕 개수를 나타냄
    seg_tree = SegmentTree([0] * (MAX_TASTE + 1), lambda x, y: x + y, 0)
    
    result = []
    
    for i in range(1, n + 1):
        query = list(map(int, data[i].split()))
        
        if query[0] == 1:
            # 사탕 꺼내기: B번째로 맛있는 사탕을 꺼냄
            B = query[1]
            low, high = 1, MAX_TASTE
            
            # 이분 탐색을 통해 B번째로 맛있는 사탕을 찾습니다.
            while low < high:
                mid = (low + high) // 2
                if seg_tree.query(1, mid + 1) >= B:  # mid까지의 사탕 개수가 B 이상이면
                    high = mid  # 더 작은 구간으로 탐색
                else:
                    low = mid + 1  # 더 큰 구간으로 탐색
            
            # 찾은 사탕을 출력하고 해당 사탕을 하나 제거
            result.append(str(low))
            seg_tree.update(low, seg_tree.query(low, low + 1) - 1)
        
        elif query[0] == 2:
            # 사탕 넣기 또는 빼기: 맛이 B인 사탕을 C개 추가 또는 제거
            B, C = query[1], query[2]
            current_count = seg_tree.query(B, B + 1)
            seg_tree.update(B, current_count + C)
    
    # 결과 출력
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()