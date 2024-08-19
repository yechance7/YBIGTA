from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""

def main() -> None:
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    test_cases = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(test_cases):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        movies_to_watch = list(map(int, data[index:index + m]))
        index += m
        
        
        # DVD의 초기 상태를 설정 (1부터 n까지의 DVD를 스택처럼 관리)
        total_size = n + m

        segment_tree: SegmentTree = SegmentTree(total_size + 1, 
                                            lambda a, b: a + b, 0)
        place = [0] * (n + 1)

        # DVD의 번호를 인덱스와 연결하여 관리
        for i in range(1, n + 1):
            place[i] = m + i
            segment_tree.update(place[i], 1)

        current_top = m
        result = []

        
        for movie in movies_to_watch:
            movie_index = place[movie]  # 0-based index로 변환
            
            # 꺼낼 때, 영화의 위에 몇 개의 DVD가 있는지 쿼리
            num_above = segment_tree.query(1, movie_index)
            result.append(str(num_above))
            
            # 꺼낸 DVD를 가장 위로 이동
            # 현재 DVD의 개수를 감소시키고, 제일 위로 이동
            segment_tree.update(movie_index, -1)  # 현재 DVD의 개수 0으로 설정
            current_top -= 1
            segment_tree.update(current_top, 1)
            place[movie] = current_top
        
        results.append(" ".join(result))

    print("\n".join(results))

if __name__ == "__main__":
    main()