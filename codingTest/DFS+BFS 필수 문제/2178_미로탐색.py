# 미로 탐색
# N×M크기의 배열로 표현되는 미로
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동

# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다

from collections import deque

n, m = map(int, input().split())

maze = []
# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n) :
    maze.append(list(map(int, input())))

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n and 0 <= ny < m) :
                if (maze[nx][ny] == 1) :
                    queue.append((nx, ny))
                    maze[nx][ny] = maze[x][y] + 1

bfs(0, 0)
print(maze[n-1][m-1])

# input
# 4 6
# 101111
# 101010
# 101011
# 111011

# result
# 15