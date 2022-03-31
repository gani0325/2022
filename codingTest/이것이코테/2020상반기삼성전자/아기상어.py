# 아기상어
# : N X N 크기 공간에 물고기 M마리와 아기상어 1마리 있다
# : 한칸에는 물고기가 최대 1마리 존재
# : 아기 상어와 물고기는 모두 크기를 가지고 있고 크기는 자연수
# : 처음 아기 상어 크기는 2, 아기 상어는 1초에 상하좌우로 이동
# : 아기 상어는 자기 자신 보다 큰 물고기를 지나갈 수 없다
# : 아기 상어는 자기 자신 보다 작은 물고기를 먹는다
# : 크기가 같은 물고기는 먹을 수 없고, 그 물고기 칸도 지갈 수 없다
# - 더이상 먹을 물고기가 없다면 엄마상어에게 SOS
# - 먹을 수 있는 물고기가 1마리라면, 먹으러 간다
# - 먹을 수 있는 물고기가 많다면, 가장 가까운 물고기로
# - 거리는 아기 상어가 물고기 칸 이동할 때, 지나갈 수 있는 개수의 최소칸
# - 거리 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그 물고기 또한 많다면, 가장 왼쪽 물고기를 먹는다
# : 아기상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기 1 증가
# = > 아기 상어가 몇 초 동안 엄마 상어에게 SOS 안하고 물고기 잡아먹을 수 있는가???

# - 최단 거리 알고리즘!! BFS

from collections import deque
INF = 1e9

n = int(input())

array = []
for i in range(n) :
    array.append(list(map(int, input().split())))

# 아기 상어 현재 크기, 현재 위치
now_size = 2
now_x, now_y = 0, 0

# 아기 상어 시작 위치, 그 위치 아무것도 없다
for i in range(n) :
    for j in range(n) :
        if array[i][j] == 9 :
            now_x, now_y = i, j
            array[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 모든 위치까지의 "최단 거리" 만 계산하는 BFS
def bfs() :
    # 값 -1이면 도달 x
    dist = [[-1] * n for _ in range(n)]
    # 시작 위치는 도달 가능, 거리 0
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0

    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and 0 <= ny and nx < n and ny < n :
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size :
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist

# 먹을 물고기
def find(dist) :
    x, y = 0, 0
    min_dist = INF
    for i in range(n) :
        for j in range(n) :
            # 도달 가능하며 먹을 수 있는 물고기
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size :
                # 가장 가까운 물고기 1마리
                if dist[i][j] < min_dist :
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF : # 없을 경우
        return None
    else :
        return x, y, min_dist

result = 0
ate = 0

while True :
    # 먹을 수 있는 물고기 위치
    value = find(bfs())
    # 없을 경우, 움직인 거리
    if value == None :
        print(result)
        break
    else :
        # 갱신 변경
        now_x, now_y = value[0], value[1]
        result += value[2]
        # 먹은 위치에는 아무것도 없이 처리
        array[now_x][now_y] = 0
        ate += 1
        # 자신의 크기 위치이상으로 먹으면! 크기 증가
        if ate >= now_size :
            now_size += 1
            ate = 0