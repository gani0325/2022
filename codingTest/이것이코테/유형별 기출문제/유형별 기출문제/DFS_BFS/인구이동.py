# 인구이동
# : N X N크기의 땅
# : 각각의 땅에는 나라가 하나씩 존재하며 r행 c열에 있는 나라에는 A[r][c] 명이 살고 있다
# : 인접한 나라 사이에 국경선 존재
# - 국경선을 공유하는 두 나라의 인구 차이가 L명 이상 R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다
# - 열어야 하는 국경선이 모두 열렸다면 인구 이동 시작
# - 국경선이 열려 있어 인접한 칸만을 이용해 이동 (그 나라를 하루 동안 연합)
# - 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
# - 연합을 해체하고, 모든 국경선 닫는다

# => 각 나라의 인구수가 주어졌을 때, 인구 이동이 몇 번 발생하는지 구해라
# BFS

from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n) :
    graph.append(list(map(int ,input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

def process(x, y, index) :
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))
    union[x][y] = index  
    summary = graph[x][y]
    count = 1

    while q : 
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <n and 0 <= ny < n and union[nx][ny] == -1 :
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united :
        graph[i][j] = summary // count
    return count

total_count = 0

while True :
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n) :
        for j in range(n) :
            if union[i][j] == -1 :
                process(i, j, index)
                index += 1
    if index == n * n :
        break
    total_count += 1

print(total_count)