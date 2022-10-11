# 안전 영역

# 재난방재청에서는 많은 비가 내리는 장마철에 대비

# 먼저 어떤 지역의 높이 정보를 파악한다.
# 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사
# 문제를 간단하게 하기 위하여, 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.

# 어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수
# 물에 잠기지 않는 안전한 영역이라 함은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 그 크기가 최대인 영역

# 어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성

# 첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. N은 2 이상 100 이하의 정수
# 둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력
# 각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력
# 높이는 1이상 100 이하의 정수

# 첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력


# 1) BFS
# from collections import deque

# def bfs(x, y, h) :
#     queue = deque()
    
#     # 시작 지점 방문 표시
#     queue.append((x, y))
#     visited[x][y] = 1

#     while queue :
#         x, y = queue.popleft()
#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]

#             # 범위 내
#             if 0 <= nx and nx < N and 0 <= ny and ny < N :
#                 # 방문한 적 없고, 기준 높이보다 크다
#                 if (visited[nx][ny] == 0) and (h < graph[nx][ny]) :
#                     # 방문 표시
#                     queue.append((nx, ny))
#                     visited[nx][ny] = 1

# N = int(input())

# graph = []
# for i in range(N) :
#     graph.append(list(map(int, input().split())))

# min_h = min(map(min, graph))
# max_h = max(map(max, graph))

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# # 최대 안전 개수
# cnt = 0

# for h in range(min_h - 1, max_h) :
#     visited = [[0] * N for _ in range(N)]
#     safe = 0    # 안전 영역 개수

#     for i in range(N) :
#         for j in range(N) :
#             # 방문 x, 높이 보다 크면
#             if (visited[i][j] == 0 and h < graph[i][j]) :
#                 bfs(i, j, h)
#                 safe += 1
#     if (safe > cnt) :
#         cnt = safe
# print(cnt)

# input
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7

# result
# 5

# 2) DFS
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y, h) :
    # 현재 지점
    visited[x][y] = 1

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < N) :
            # 방문한적 없고, 높이보다 크다
            if (visited[nx][ny] == 0) and (h < graph[nx][ny]) :
                visited[nx][ny] = 1     # 방문처리
                dfs(nx, ny, h)

N = int(input())    

graph = []
for i in range(N) :
    graph.append(list(map(int, input().split())))

min_h = min(map(min, graph))
max_h = max(map(max, graph))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 최대 안전영역 개수
cnt = 0

# 높이 변수를 0부터 100까지 설정
for h in range(101) :
    visited = [[0] * N for _ in range(N)]
    safe = 0    # 안전영역 개수

    for i in range(N) :
        for j in range(N) :
            # 방문 안하고, 높이 이상이면
            if (visited[i][j] == 0) and (graph[i][j] > h) :
                dfs(i, j, h)
                safe += 1

    if (safe > cnt) :
        cnt = safe
print(cnt)

# input
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7

# result
# 5