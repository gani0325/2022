# 단지번호붙이기
# 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성

# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력

# 첫 번째 줄에는 총 단지수를 출력. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력

# 1) DFS
# def dfs(x, y) :
#     global house_cnt

#     if x < 0 or x > n-1 or y < 0 or y > n-1 :       # 지도 밖
#         return False
    
#     if graph[x][y] == False :        # 집 없음
#         return False

#     else :
#         graph[x][y] = 0
#         house_cnt += 1      # 집 있으면 누적

#         for idx in range(4) :       # 재귀적 방문
#             nx = x + dx[idx]
#             ny = y + dy[idx]
#             dfs(nx, ny)

#         return True

# n = int(input())
# graph = [list(map(int, input())) for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# house_cnt = 0
# total_cnt = 0
# result = []


# for i in range(n) :
#     for j in range(n) :
#         if dfs(i, j) :      # 결과가 True 이면!
#             result.append(house_cnt)
#             house_cnt = 0
#             total_cnt += 1

# print(total_cnt)
# for i in sorted(result) :       # 오름차순
#     print(i)

# # input
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# # result
# 3
# 7
# 8
# 9


# 2) BFS
from collections import deque

n = int(input())
graph = []
result = []

for _ in range(n) :
    graph.append(list(map(int, input())))

def bfs(x, y) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    graph[x][y] = 0
    count = 1

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] == 1 :
                graph[nx][ny] = 0           # 초기화
                queue.append((nx, ny))
                count += 1

    result.append(count)

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            bfs(i, j)

print(len(result))
for i in sorted(result) :
    print(i)

# # input
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# # result
# 3
# 7
# 8
# 9