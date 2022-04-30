# 2048(easy)

# 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것
# 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다.
# 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.
# (실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만,
# 이 문제에서 블록이 추가되는 경우는 없다)

# 똑같은 수가 세 개가 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐진다.
# 예를 들어, 위로 이동시키는 경우에는 위쪽에 있는 블록이 먼저 합쳐지게 된다.

# 이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다.
# 보드의 크기와 보드판의 블록 상태가 주어졌을 때,
# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램

from collections import deque
n = int(input())
board = []
for i in range(n) :
    board.append(list(map(int, input().split())))
answer = 0
q = deque()


def get(i, j) :
    if board[i][j] :
        q.append(board[i][j])
        board[i][j] = 0

def merge(i, j, di, dj):  # row, column, y방향, x 방향
    while q:
        x = q.popleft()
        if not board[i][j]:
            board[i][j] = x
        elif board[i][j] == x:
            board[i][j] = x * 2
            i, j = i + di, j + dj
        else:
            i, j = i + di, j + dj
            board[i][j] = x

def move(k) :
    if k == 0 :     # 위
        for j in range(n) :
            for i in range(n) :
                get(i, j)
            merge(0, j, 1, 0)
    elif k == 1 :   # 아래
        for j in range(n) :
            for i in range(n-1, -1, -1) :
                get(i, j)
            merge(n-1, j, -1, 0)
    elif k == 2 :   # 오른
        for i in range(n) :
            for j in range(n) :
                get(i, j)
            merge(i, 0, 0, 1)
    else :    # 왼
        for i in range(n) :
            for j in range(n-1, -1, -1) :
                get(i, j)
            merge(i, n-1, 0, -1)


def solve(count) :
    global board, answer
    if count == 5 :
        for i in range(n) :
            answer = max(answer, max(board[i]))
        return
    b = [x[:] for x in board]

    for k in range(4) :
        move(k)
        solve(count+1)
        board = [x[:] for x in b]

solve(0)
print(answer)



