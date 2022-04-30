# 마법사 상어와 블리자드
# N은 항상 홀수이고, (r, c)는 격자의 r행 c열을 의미한다. 격자의 가장 왼쪽 윗 칸은 (1, 1)이고,
# 가장 오른쪽 아랫 칸은 (N, N)이며 마법사 상어는 ((N+1)/2, (N+1)/2)

# 방향 di와 거리 si를 정해야 한다. 총 4가지 방향 ↑, ↓, ←, →가 있고, 정수 1, 2, 3, 4
# 상어는 di 방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴한다.
# 구슬이 파괴되면 그 칸은 구슬이 들어있지 않은 빈 칸이 된다.
# 얼음 파편은 벽의 위로 떨어지기 때문에, 벽은 파괴되지 않는다.

# 폭발하는 구슬은 4개 이상 연속하는 구슬이 있을 때 발생
# 구슬이 이동한 후에는 다시 구슬이 폭발하는 단계이고,
# 이 과정은 더 이상 폭발하는 구슬이 없을때까지 반복

# 구슬이 변화하는 단계가 된다. 연속하는 구슬은 하나의 그룹

# 하나의 그룹은 두 개의 구슬 A와 B로 변한다.
# 구슬 A의 번호는 그룹에 들어있는 구슬의 개수이고, B는 그룹을 이루고 있는 구슬의 번호

# 총 M번 시전했다. 시전한 마법의 정보가 주어졌을 때,
# 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)

from collections import deque

def check_range(y, x) :
    return (0 <= y < N) and (0 <= x < N)

def make_order_map() :
    y = N // 2
    x = N // 2
    order_pos.append((y, x))
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    cd = 0
    step = 0
    while True :
        if cd % 2 == 0 :
            step += 1
        flag = True
        for _ in range(step) :
            y += dy[cd]
            x += dx[cd]
            order_pos.append((y, x))
            if y == 0 and x == 0 :
                flag = False
                break
        if not flag :
            break
        cd = (cd + 1) % 4

# 빈칸 채우기
def move_to_empty(board) :
    move_pos = deque()

    for y, x in order_pos :
        if y == N // 2 and x == N // 2 :
            continue
        if board[y][x] == 0 :
            move_pos.append((y, x))
        elif board[y][x] > 0 and move_pos :
            my, mx = move_pos.popleft()
            board[my][mx], board[y][x] = board[y][x], 0
            move_pos.append((y, x))

# 같은 숫자 연속 4개
def find_4_numbers(board) :
    visited = deque()
    count = 0
    number = -1
    flag = False
    for y, x in order_pos :
        if y == N // 2 and x == N // 2 :
            continue

        if number == board[y][x] :
            visited.append((y, x))
            count += 1
        else :
            if count >= 4 :
                flag = True
                scores[number] += count
            while visited :
                ny, nx = visited.popleft()
                if count >= 4 :
                    board[ny][nx] = 0
            count = 1
            number = board[y][x]
            visited.append((y, x))
    return flag

# 해당 숫자 몇 번
def make_group(board) :
    number = -1
    count = 0
    numbers = [0]
    for y, x in order_pos :
        if y == N // 2 and x == N // 2 :
            continue

        if number == -1 :
            number = board[y][x]
            count = 1
        else :
            if number == board[y][x] :
                count += 1
            else :
                numbers.append(count)
                numbers.append(number)
                number = board[y][x]
                count = 1

    idx = 0
    for y, x in order_pos :
        board[y][x] = numbers[idx]
        idx += 1
        if idx >= len(numbers) :
            break


def solve(board, m) :
    if m == M :
        return

    D, S = cmd[m][0], cmd[m][1]
    cy = cx = N // 2
    for s in range(1, S+1) :
        ny = cy + (s * dy[D])
        nx = cx + (s * dx[D])
        if check_range(ny, nx) :
            board[ny][nx] = 0
    # 빈칸 채우기
    move_to_empty(board)
    # 연속된 숫자 4개
    while find_4_numbers(board) :
        move_to_empty(board)

    # 번호 그룹, 개수-번호
    make_group(board)
    solve(board, m+1)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
order_pos = []
cmd = []
scores = [0, 0, 0, 0]
for _ in range(M):
    d, s = map(int, input().split())
    cmd.append((d, s))

make_order_map()
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]
solve(board, 0)
answer = 0
for i in range(1, 4):
    answer += (i*scores[i])

print(answer)