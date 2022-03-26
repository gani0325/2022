# 경쟁적 전염
# : N X N 크기의 시험관
# : 바이러스는 1 ~ K까지 있으며 1초마다 상, 하, 좌 ,우 로 증식한다
# : 매초 번호가 낮은 바이러스부터 먼저 증식
# : 특정 칸에 바이러스 있다면 다른 바이러스 들어갈 수 없다.
# : 시험관의 크기와 바이러스 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램은?
# : 낮은 번호므로 큐 삽입

from collections import deque


n, k = map(int, input().split())


graph = []
data = []

for i in range(n) :
    graph.append(list(map(int, input().split())))
    for j in range(n) :
        if graph[i][j] != 0 :
            data.append((graph[i][j], 0, i, j))
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS
while q :
    virus, s, x, y = q. popleft()
    if s == target_s :
        break

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 < nx and nx < n and 0 < ny and ny < n :
            if graph[nx][ny] == 0 :
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x - 1][target_y - 1])

