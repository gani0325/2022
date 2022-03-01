# 1.미로 탈출
# : N X M 크기의 직사각형 미로에 갇힘
# : 나의 위치는 (1, 1) 미로의 출구는 (N, M)
# : 괴물이 있는 부분은 0, 괴물 없는 부분은 1
# : 탈출하기 위해 움직여야 하는 최소의 칸 개수

# BFS 이용
# : 시작지점에서 가까운 노드부터 차례대로 그래프의 모든 노트 탐색
# : (1,1)에서 BFS 수행하여 모든 노드의 값을 거리 정보로 넣기
# : 특정 노드 방문하면 이전 노드에 1 더해서 리스트에 넣기

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue = deque()
    queue.append((x,y))

    # 큐 빌 때까지 반복
    while queue : 
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 벗어나면 무시
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m :
                continue
            # 벽이면 무시
            if graph[nx][ny]==0 :
                continue
            # 해당 노드 처음 방문하면 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래 최단 거리 반환
    return graph[n-1][m-1]
print(bfs(0, 0))
            