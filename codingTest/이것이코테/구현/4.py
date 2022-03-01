# 4. 게임 개발
# 캐릭터는 1x1 정사각형으로 이뤄진 N X M 직사각형에 있음
# 맵의 각 칸은 (A,B)이고 A는 북쪽으로부터 떨어진 칸의 개수, B는 서족으로부터 떨어진 칸의 개수
# 각각의 칸은 육지, 바다로 되어 있음. 바다로는 못간다
# - 현재 방향 기준으로 왼쪽 방향( 반시계로 90도 회전 방향 )부터 차례대로 갈 곳 정함
# - 바로 왼쪽 방향에 아직 안가본 칸 존재하면, 왼쪽으로 회존한 다음 왼쪽으로 한 칸 전진
# - 아직 안가본 칸이 없다면, 왼쪽 방향으로 회전만 하고 1단계로 ㄱ
# - 네 방향 모두 가본 곳이거나 바다면, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 ㄱ ( 뒤가 바다라면 움직임 멈춤)
# 캐릭터가 방문한 칸의 수 출력
# 0: 북, 1 : 동, 2: 남, 3 : 서
# 0: 육지, 1 : 바다

n, m = map(int, input().split())

d = [[0] * m for _ in range(n) ]

x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

array = []
for i in range(n) :
    array.append(list(map(int, input().split())))
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전
def turn_left() :
    global direction
    direction -= 1
    if direction == -1 :
        direction = 3

cnt = 1
turn_time = 0
while True :
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 가보지 않은 곳
    if d[nx][ny] == 0 and array[nx][ny] == 0 :
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue

    # 가봤거나 바다
    else :
        turn_time += 1
    
    # 네 방향 모두 갈수 없음
    if turn_time == 4 :
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있으면
        if array[nx][ny] == 0 :
            x = nx
            y = ny
        else :
            break

        turn_time = 0
print(cnt)