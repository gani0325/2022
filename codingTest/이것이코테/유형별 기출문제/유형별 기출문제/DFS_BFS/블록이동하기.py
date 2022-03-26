# 블록 이동하기
# : 2 x 1 크기의 로봇으로 무지는 '0'과 '1'로 이루어진 N X N 크기의 지도에서 2 X 1크기인 로봇을 움직여 (N, N) 위치까지 이동시키고자 한다
# : 0은 빈칸, 1은 벽
# : 1,1 위치에서 가로 방향으로 놓인채 움직인다 앞뒤 구분 없다

# => 로봇이 N,N 위치에 이동하는데 필요한 최소 시간
# => 로봇이 존재할 수 있는 각 위치를 노드, 인접한 위치와 비용을 1인 간선
# => BFS 통해 최단 거리 계산

from collections import deque

def get_next_pos(pos, board) :
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4) :
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0 :
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    if pos1_x == pos2_x :
        for i in [-1, 1] :
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0 :
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    elif pos1_y == pos2_y :
        for i in [-1, 1] :
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0 :
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    return next_pos

def solution(board) :
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n) :
        for j in range(n) :
            new_board[i+1][j+1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)

    while q :
        pos, cost = q.popleft()
        if (n, n) in pos :
            return cost

        for next_pos in get_next_pos(pos, new_board) :
            if next_pos not in visited :
                q.append((next_pos, cost+1))
                visited.append(next_pos)
    return 0