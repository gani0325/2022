# 마법사 상어와 비바라기
# (r, c)는 격자의 r행 c열에 있는 바구니를 의미하고,
# A[r][c]는 (r, c)에 있는 바구니에 저장되어 있는 물의 양
# 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름 생김

# 구름에 이동을 M번 명령하려고 한다. i번째 이동 명령은 방향 di과 거리 si로 이루어져 있다.
# 방향은 총 8개의 방향이 있으며, 8개의 정수로 표현한다.
# 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙

# 1. 모든 구름이 di 방향으로 si칸 이동한다.
# 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
# 3. 구름이 모두 사라진다.
# 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다.
    # 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼
    # (r, c)에 있는 바구니의 물이 양이 증가한다.
    # 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
    # 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
# 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = [tuple(map(int, input().split())) for _ in range(m)]

# 8방향
dy8 = ("empty", 0, -1, -1, -1, 0, 1, 1, 1)
dx8 = ("empty", -1, -1, 0, 1, 1, 1, 0, -1)

dx4 = (-1, 1, 1, -1)
dy4 = (1, 1, -1, -1)

clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for d, s in moves :
    moved_cloud = []
    for y, x in clouds :
        # 구름들을 d방향으로 s 만큼
        ny = (y + dy8[d] * s ) % n
        nx = (x + dx8[d] * s ) % n
        board[ny][nx] += 1      # 물 양 추가
        moved_cloud.append((ny, nx))

    for y, x in moved_cloud :
        # 대각 4방향
        cnt = 0
        for d in range(4) :
            ny = y + dy4[d]
            nx = x + dx4[d]
            if nx < 0 or nx >= n or 0 > ny or ny >= n :
                continue
            elif board[ny][nx] > 0 :
                cnt += 1
        board[y][x] += cnt

    new_clouds = []
    for y in range(n) :
        for x in range(n) :
            if (y, x) in moved_cloud or board[y][x] < 2 :
                continue
            board[y][x] -= 2
            new_clouds.append((y, x))
    clouds = new_clouds

result = 0
for y in range(n) :
    for x in range(n) :
        result += board[y][x]
print(result)







