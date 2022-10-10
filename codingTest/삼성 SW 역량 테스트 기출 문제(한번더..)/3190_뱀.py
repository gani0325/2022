# 뱀

# 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다.
# 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다.
# 보드의 상하좌우 끝에 벽이 있다.
# 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다.
# 뱀은 처음에 오른쪽을 향한다.

# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
#     먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
#     만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
#     만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
#       즉, 몸길이는 변하지 않는다.
#     사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미
#     사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 
# 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전
# X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

# 첫째 줄에 게임이 몇 초에 끝나는지 출력

# 1) BFS
from collections import deque

N = int(input())
K = int(input())

# 맵 정보 (사과가 있는 곳은 1)
apple = [[0] * (N+1) for _ in range(N+1)]
for _ in range(K):
    a, b = map(int, input().split())
    apple[a][b] = 1

direction = []
L = int(input())
for i in range(L) :
    # 정수 X, 문자 C
    x, c = input().split()
    direction.append((int(x), c))

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(d, c) :
    # 왼쪽으로, 상 좌 하 우
    # 오른쪽으로, 상 우 하 좌
    if c == "D" :
        d = (d + 1) % 4
    else :
        d = (d - 1) % 4
    return d

def bfs() :
    # 초기 방향
    dd = 0
    # 초기 시간
    tt = 0
    # 다음에 회전할 정보
    index = 0 
    # 뱀 위치
    x, y = 1, 1
    apple[x][y] = 2
    # 방문 위치
    q = [(x, y)]
    # q.append((x, y))

    while True :
        ny = y + dy[dd]
        nx = x + dx[dd]
        
        # 방문 안한곳 0, 사과 1, 방문한곳2
        if 1 <= ny <= N and 1 <= nx <= N and apple[nx][ny] != 2 :
            # 사과 없음
            if apple[nx][ny] == 0 :
                # 꼬리 제거
                apple[nx][ny] = 2
                q.append((nx, ny))
                # 이동 좌표 변환
                px, py = q.pop(0)
                apple[px][py] = 0

            # 사과 있음
            if apple[nx][ny] == 1 :
                apple[nx][ny] = 2
                q.append((nx, ny))
        # 부딪히면
        else :
            tt += 1
            break
        # 다음 위치로 머리 이동
        x, y = nx, ny
        tt += 1

        if index < L and tt == direction[index][0] :
            dd = turn(dd, direction[index][1])
            index += 1

    return tt
print(bfs())

# input
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# output
# 9