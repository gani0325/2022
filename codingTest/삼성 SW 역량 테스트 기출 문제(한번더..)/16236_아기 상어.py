    # 아기상어

# N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 
# 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재

# 아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다.
# 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동

# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 
# 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
    # 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

# 아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청
    # 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
    # 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 
    # 가장 왼쪽에 있는 물고기를 먹는다.
# 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정
    # 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다
    # 물고기를 먹으면, 그 칸은 빈 칸이 된다.
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 

# 공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는가

# 첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.
# 둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이뤄짐
    # 0: 빈 칸
    # 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
    # 9: 아기 상어의 위치
# 아기 상어는 공간에 한 마리 있다.

# 첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력

# 1) BFS
from collections import deque

N = int(input())
graph = []
for i in range(N) :
    graph.append(list(map(int, input().split())))

now_size = 2
now_x, now_y = 0, 0

for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 9 :
            now_x, now_y = i, j
            graph[i][j] = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs() :
    dist = [[-1] * N for _ in range(N)]
    q = deque()
    # 아기 상어 위치
    q.append([now_x, now_y])
    dist[now_x][now_y] = 0

    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N :
                # 방문 안했고, 아기상어보다 작은 물고기!
                if dist[nx][ny] == -1 and graph[nx][ny] <= now_size :
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

def find(dist) :
    x, y = 0, 0
    min_dist = 1e9

    for i in range(N) :
        for j in range(N) :
            # 먹을 수 있는 물고기가 많다면...
            if dist[i][j] != -1 and 1 <= graph[i][j] and graph[i][j] < now_size :
                # 가장 가까운
                if dist[i][j] < min_dist :
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == 1e9 :
        return None
    else :
        return x, y, min_dist

result = 0
ate = 0

while True :
    value = find(bfs())

    if value == None :
        print(result)
        break
    else :
        now_x, now_y = value[0], value[1]
        result += value[2]

        graph[now_x][now_y] = 0
        ate += 1
        if ate >= now_size :
            now_size += 1
            ate = 0