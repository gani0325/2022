# 뱀

# 뱀은 매 초마다 이동
# 사과를 먹으면 뱀 길이가 늘어난다
# 자기자신의 몸과 부딪히면 게임이 끝난다.

# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면,
# 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면,
# 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
# 즉, 몸길이는 변하지 않는다.

# 사과의 위치와 뱀의 이동경로가 주어질 때
# 이 게임이 몇 초에 끝나는지 계산하라.

# 보드 크기
n = int(input())
# 사과 개수
k = int(input())

apple = [[0] * (n+1) for _ in range(n+1)]

# 사과 위치 행 열
for i in range(k) :
    a, b = map(int, input().split())
    apple[a][b] = 1

# 뱀 방향 변환 횟수
l = int(input())
# 뱀 방향 변환 정보 (L은 왼쪽, D는 오른쪽 90도 방향 회전)
snake = []
for _ in range(l) :
    x, c = input().split()
    snake.append((int(x), c))

# 처음은 오른쪽. 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# dx = [1, 0, -1, 0]
# dy = [0, -1, 0, 1]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    apple[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q =[(x, y)]

    while True :
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and apple[nx][ny] != 2 :
            if apple[nx][ny] == 0 :
                apple[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                apple[px][py] = 0

            if apple[nx][ny] == 1 :
                apple[nx][ny] = 2
                q.append((nx, ny))

        else :
            time += 1
            break
        x, y = nx, ny
        time += 1

        if index < l and time == snake[index][0] :
            direction = turn(direction, snake[index][1])
            index += 1
    return time

print(simulate())

