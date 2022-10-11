# 송도에 사는 상근이와 친구들은 송도에서 열리는 펜타포트 락 페스티벌에 가려고 한다. 
# 올해는 맥주를 마시면서 걸어가기로 했다.
# 출발은 상근이네 집에서 하고, 맥주 한 박스를 들고 출발한다.
# 맥주 한 박스에는 맥주가 20개 들어있다. 

# 목이 마르면 안되기 때문에 50미터에 한 병씩 마시려고 한다. 
# 즉, 50미터를 가려면 그 직전에 맥주 한 병을 마셔야 한다.

# 맥주를 더 구매해야 할 수도 있다.
# 편의점에 들렸을 때, 빈 병은 버리고 새 맥주 병을 살 수 있다.
# 박스에 들어있는 맥주는 20병을 넘을 수 없다. 
# 편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 한다.

# 편의점, 상근이네 집, 펜타포트 락 페스티벌의 좌표가 주어진다. 
# 상근이와 친구들이 행복하게 페스티벌에 도착할 수 있는지 구하는 프로그램을 작성

# 첫째 줄에 테스트 케이스의 개수 t가 주어진다. (t ≤ 50)
# 각 테스트 케이스의 첫째 줄에는 맥주를 파는 편의점의 개수 n이 주어진다. (0 ≤ n ≤ 100).

# 다음 n+2개 줄에는 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표가 주어진다. 
# 각 좌표는 두 정수 x와 y로 이루어져 있다. (두 값 모두 미터, -32768 ≤ x, y ≤ 32767)

# 송도는 직사각형 모양으로 생긴 도시이다. 
# 두 좌표 사이의 거리는 x 좌표의 차이 + y 좌표의 차이 이다. (맨해튼 거리)

# 각 테스트 케이스에 대해서 상근이와 친구들이 행복하게 페스티벌에 갈 수 있으면 "happy",
# 중간에 맥주가 바닥나서 더 이동할 수 없으면 "sad"를 출력

# 1) BFS
from collections import deque

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))

    visited = [(x, y)]

    while queue :
        x, y = queue.popleft()
        visited.append((x, y))

        if x == rock_x and y == rock_y :
            print("happy")
            return
        
        for nx, ny in graph :
            if (nx, ny) not in visited :
                if abs(nx - x) + abs(ny - y) <= beer * 50 :
                    queue.append((nx, ny))
                    visited.append((nx, ny))
    print("sad")
    return


visited = []
# 테스트 케이스 개수
t = int(input())

for i in range(t) :
    # 맥주 개수
    beer = 20

    # 편의점 개수
    n = int(input())

    # 집
    home_x, home_y = map(int, input().split())
    graph = []

    # 편의점
    for j in range(n) :
        x, y = map(int, input().split())
        graph.append((x, y))

    rock_x, rock_y = map(int, input().split())
    graph.append((rock_x, rock_y))

    bfs(home_x, home_y)


# input
# 2
# 2
# 0 0
# 1000 0
# 1000 1000
# 2000 1000

# output
# happy


# input
# 2
# 0 0
# 1000 0
# 2000 1000
# 2000 2000

# output
# sad
