from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""

def main() -> None:
    # 입력을 처리합니다.
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])  # 수정이가 사탕상자에 손을 댄 횟수
    
    # 세그먼트 트리 초기화
    # 세그먼트 트리에서 각 인덱스는 특정 맛의 사탕 개수를 나타냄
    size = 2**20
    seg_tree: SegmentTree[int, int] = SegmentTree(size, lambda x, y: x + y, 0)
    index = 1
    
    
    for _ in range(n):
        query = int(data[index])
        
        if query == 1:
            # 사탕 꺼내기: B번째로 맛있는 사탕을 꺼냄
            B = int(data[index + 1])
            kth_candy = seg_tree.find_kth(B)
            print(kth_candy)
            seg_tree.update(kth_candy, -1)
            index += 2
            
        
        elif query == 2:
            # 사탕 넣기 또는 빼기: 맛이 B인 사탕을 C개 추가 또는 제거
            B, C = int(data[index + 1]), int(data[index + 2])
            seg_tree.update(B, C)
            index +=3
    

if __name__ == "__main__":
    main()