# 주사위 굴리기

# 주사위는 지도 위에 윗 면이 1이고,
# 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며,
# 놓여져 있는 곳의 좌표는 (x, y) 이다.

# 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.
# 지도의 각 칸에는 정수가 하나씩 쓰여져 있다.
# 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면,
# 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
# 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며,
# 칸에 쓰여 있는 수는 0이 된다.

# 주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때,
# 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성하시오.

# 주사위는 지도의 바깥으로 이동시킬 수 없다.
# 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며,
# 출력도 하면 안 된다.

# 첫째 줄에 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20),
# 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1),
# 명령의 개수 K (1 ≤ K ≤ 1,000)가 주어진다.

# 둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로,
# 각 줄은 서쪽부터 동쪽 순서대로 주어진다.
# 주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다.
# 지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.


n, m, x, y, k = map(int, input().split())
board = []

for i in range(n) :
    board.append(list(map(int, input().split())))

command = list(map(int, input().split()))

direction = [
    (2, 0, 5, 3, 4, 1),
    (1, 5, 0, 3, 4, 2),
    (4, 1, 2, 0, 5, 3),
    (3, 1, 2, 5, 0, 4)
]

# direction = [
#     [2, 0, 5, 3, 4, 1],
#     [1, 5, 0, 3, 4, 2],
#     [4, 1, 2, 0, 5, 3],
#     [3, 1, 2, 5, 0, 4]
# ]

dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)



dice = [0] * 6
temp = [0] * 6

for c in command :
    c -= 1
    x = x + dx[c]
    y = y + dy[c]

    if x < 0 or x >= n or y < 0 or y >= m :
        x = x - dx[c]
        y = y - dy[c]
        continue

    for i in range(6) :
        temp[i] = dice[i]
    for i in range(6) :
        dice[i] = temp[direction[c][i]]
    if board[x][y] :
        dice[5] = board[x][y]
        board[x][y] = 0
    else :
        board[x][y] = dice[5]
    print(dice[0])
