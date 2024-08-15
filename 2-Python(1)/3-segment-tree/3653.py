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
        dvd_count = [1] * n
        segment_tree = SegmentTree(dvd_count, 
                                   operation=lambda x, y: x + y, 
                                   default=0)
        
        # DVD의 번호를 인덱스와 연결하여 관리
        dvd_position = list(range(n))
        
        for movie in movies_to_watch:
            movie_index = movie - 1  # 0-based index로 변환
            
            # 꺼낼 때, 영화의 위에 몇 개의 DVD가 있는지 쿼리
            num_above = segment_tree.query(0, movie_index)
            results.append(num_above)
            
            # 꺼낸 DVD를 가장 위로 이동
            # 현재 DVD의 개수를 감소시키고, 제일 위로 이동
            if movie_index > 0:
                segment_tree.update(movie_index, 0)  # 현재 DVD의 개수 0으로 설정
                segment_tree.update(movie_index - 1, segment_tree.query(movie_index - 1, movie_index - 1) + 1)
            segment_tree.update(0, 1)  # 맨 위로 이동

    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()