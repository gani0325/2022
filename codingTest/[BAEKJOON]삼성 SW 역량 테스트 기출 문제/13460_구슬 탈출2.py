# 구슬 탈출 2

# 보드의 세로 크기는 N, 가로 크기는 M이고,
# 편의상 1×1크기의 칸으로 나누어져 있다.
# 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다.

# 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다.
# 이때, 파란 구슬이 구멍에 들어가면 안 된다.

# 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다.
# 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기

# 각각의 동작에서 공은 동시에 움직인다.
# 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다.
# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.

# 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다.
# 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

# 보드의 상태가 주어졌을 때,
# 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램

# '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며,
# 'O'는 구멍의 위치를 의미한다. 'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치
# 입력되는 모든 보드의 가장자리에는 모두 '#'이 있다.
# 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개

# 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1

from collections import deque

n, m = map(int, input().split())
map = []

for i in range(n) :
    map.append(list(input().strip()))

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()

def init() :
    rx, ry, bx, by = [0] * 4

    for i in range(n):
        for j in range(m):
            if map[i][j] == "R":
                ry = j
                rx = i
            elif map[i][j] == "B":
                by = j
                bx = i
    q.append((rx, ry, bx, by, 1))       # 위치정보, depth
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy) :
    count = 0

    while map[x+dx][y+dy] != "#" and map[x][y] != "O" :
        x += dx
        y += dy
        count += 1
    return x, y, count

def bfs() :
    init()
    while q :
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10 :
            break
        for i in range(4) :
            nrx, nry, nrc = move(rx, ry, dx[i], dy[i])
            nbx, nby, nbc = move(bx, by, dx[i], dy[i])

            if map[nbx][nby] == "O" :
                continue
            if map[nrx][nry] == "O" :
                print(depth)
                return
            if nrx == nbx and nry == nby :
                if nrc > nbc :
                    nrx -= dx[i]
                    nry -= dy[i]
                else :
                    nbx -= dx[i]
                    nby -= dy[i]

            if not visited[nrx][nry][nbx][nby] :
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, depth + 1))
    print(-1)

bfs()
