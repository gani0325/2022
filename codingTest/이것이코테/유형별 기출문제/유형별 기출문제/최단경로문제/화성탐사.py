# 화성탐사
# : 에너지를 효율적으로 사용하고자 화성 탐사 기계가 출발지점에서 목표지점까지 이동할 때 항상 최적의 경로를 찾아라

# : N X N 크기의 2차원 공간, 각각의 칸을 지나기 위한 비용 (에너지 소모량) 존재
# : 가장 위쪽 위 칸인 [0][0]위치에서 가장 오른쪽 아래 칸인 [N-1][N-1] 위치로 이동하는 최소 비용을 출력
# : 화성 탐사 기계는 특정한 위치에서 상하좌우 인접한 곳으로 1칸씩 이동 가능

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range(int(input())) :
    n = int(input())

graph = []
for i in range(n) :
    graph.append(list(map(int, input().split())))

# 최단 거리 모두 무한으로 초기화
distance = [[INF] * n for _ in range(n)]

x, y = 0, 0
q = [(graph[x][y], x, y)]
distance[x][y] = graph[x][y]

# 다익스트라
while q :
    dist, x, y = heapq.heappop(q)
    if distance[x][y] < dist :
        continue

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n :
            continue

        cost = dist + graph[nx][ny]
        if cost < distance[nx][ny] :
            distance[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))

print(distance[n-1][n-1])

