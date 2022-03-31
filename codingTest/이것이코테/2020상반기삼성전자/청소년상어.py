# 청소년 상어
# : 4 X 4 크기의 공간
# : x는 행, y는 열
# : 한칸에 물고기 1마리, 각 물고기는 번호와 방향 가짐
# : 번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수, 두 물고기가 같은 번호를 갖는 경우는 없다 
# : 방향은 8가지 방향 (상하좌우, 대각선)
# : 청소년 상어는 (0,0) 물고기 먹고 (0,0)에 들어가는데 먹은 물고기의 방향과 같다
# : 물고기는 번호가 작은 물고기부터 순서대로 이동
# : 물고기는 한 칸을 이동할 수 있고, 이동할 수 있는 칸은 빈칸과 다른 물고기가 있는 칸이고, 이동할 수 없는 칸은 상어가 있거나 공간의 경계를 넘는 칸
# : 각각의 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 방향으로 회전
# : 이동할 수 있는 칸이 없으면 이동 X, 그외는 이동
# : 물고기가 다른 물고기가 있는 칸으로 이동할 때 서로의 위치를 바꾼다

# : 물고기의 이동 모두 끝나면 상어가 이동
# : 상어는 방향에 있는 칸으로 이동, 한 번에 여러개 칸 이동 가능
# : 물고기 있는 칸에 가면 물고기 먹고, 그 방향 가짐
# : 이동 중 지나가는 칸의 물고기는 먹지 않고, 물고기 없는 곳은 갈 수 없다
# : 상어가 이동할 수 있는 칸이 없으면 집으로 간다 (이동 후 물고기가 다시 이동)

# => 상어 움직임후, 상어가 먹을 수 있는 물고기 번호의 합 최대값은??

# : 시뮬레이션과 완전 탐색!! DFS

import copy

array = [[None] * 4 for _ in range(4)]

for i in range(4) :
    data = list(map(int, input().split()))

    for j in range(4) :
        # 각 위치마다 [물고기 번호, 방향] 저장
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 현재 위치에서 왼쪽으로 회전
def turn_left(direction) :
    return (direction + 1) % 8

result = 0

# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array, index) :
    for i in range(4) :
        for j in range(4) :
            if array[i][j] == index :
                return (i, j)
    return None

# 모든 물고기를 회전 및 이동
def move_all_fishes(array, now_x, now_y) :
    # 1번부터 16번 물고기
    for i in range(1, 17) :
        # 해당 물고기 위치
        position = find_fish(array, i)
        if position != None :
            x, y = position[0], position[1]
            direction = array[x][y][1]
            # 해당 물고기 방향을 왼쪽으로 계속 회전.
            for j in range(8) :
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 해당 방향으로 이동 가능하면 이동
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4 :
                    if not (nx == now_x and ny == now_y) :
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break

                direction = turn_left(direction)

# 상어가 현재 위치에서 먹을 수 있는 모든 물고기 위치 반환
def get_possible_positions(array, now_x, now_y) :
    positions = []
    direction = array[now_x][now_y][1]
    # 현재 방향으로 계속 이동
    for i in range(4) :
        now_x += dx[direction]
        now_y += dy[direction]
        # 범위 
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4 :
            # 물고기가 존재
            if array[now_x][now_y] != -1 :
                positions.append((now_x, now_y))
    return positions

# 모든 경우 탐색 DFS
def dfs(array, now_x, now_y, total) :
    global result
    array = copy.deepcopy(array) # 복사

    total += array[now_x][now_y][0] # 현재 물고기 먹기
    array[now_x][now_y][0] = -1 # 먹었으니 -1로

    move_all_fishes(array, now_x, now_y) # 전체 물고기 이동

    # 상어 이동 차례
    positions = get_possible_positions(array, now_x, now_y)
    # 이동 없다면 종료
    if len(positions) == 0 :
        result = max(result, total)
        return
    # 모든 이동할 수 있는 위치로 재귀적 수행
    for next_x, next_y in positions :
        dfs(array, next_x, next_y, total)

dfs(array, 0, 0, 0)
print(result)
            
    

