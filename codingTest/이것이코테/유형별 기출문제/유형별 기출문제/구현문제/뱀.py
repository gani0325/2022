# 뱀
# : N X N 정사각 보드 위에서 게임 진행
# : 사과 먹으면 뱀 길이 늘어남. 벽 OR 자기 몸 부딪히면 게임종료
# - 뱀은 몸길이를 늘려 머리를 다음 칸에 위치
# - 이동한 칸에 사과가 있다면, 그 칸에 있던 사과는 없어지고, 꼬리는 움직이지X
# - 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌(몸길이 변하지 X)
# : 처음 뱀 길이는 1, 오른쪽 향함
# : 사과의 위치와 뱀의 이동 경로가 주어질 때, 게임이 몇 초에 끝나는지 계산
# 입력
# - 보드의 크기 N
# - K개줄에 사과의 위치 주어짐 (행, 열)
# - 뱀의 방향 변환 횟수 L
# - 뱀의 방향 변환 정보 (X, C)  D -> 오른쪽 90도, L -> 왼쪽 90도

n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)]
info = []  # 방향정보

# 사과 정보 1
for _ in range(k) :
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향회전
l = int(input())
for _ in range(l) :
    x, c = input().split()
    info.append((int(x), c))

# 처음은 오른쪽. 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c) :
    if c == "L" : 
        direction = (direction - 1) % 4
    else :
        direction = (direction + 1) % 4
    return direction

def simulate() :
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]

    while True :
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2 :
        # 사과 없다면 이동 후 꼬리 제거
            if data[nx][ny] == 0 :
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0

        # 사과 있다면 꼬리 두기
            if data[nx][ny] == 1 :
                data[nx][ny] = 2
                q.append((nx, ny))

        # 부딪히면
        else :
            time += 1
            break

        x, y = nx, ny
        time += 1
        if index < 1 and time == info[index][0] :
            direction = turn(direction, info[index][1])
            index += 1

    return time

print(simulate())
  
      