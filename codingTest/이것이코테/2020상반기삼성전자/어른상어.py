# 어른 상어
# : 상어 사는 공간에 더이상 물고기는 없다
# : 상어는 1 이상 M 이하의 자연수가 있고 모두 번호가 다르다
# : 1 어른 상어는 가장 강력해서 나머지를 쫓아낼 수 있다
# : N X N 격자 중 M개의 칸에 상어가 1마리씩 있다
# : 맨 처음 모든 상어가 자신의 위치에 자신의 냄새 뿌린다
# : 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고 자신의 냄새를 뿌린다
# : 냄새는 상어가 K번 이동하면 사라진다
# : 각각의 상어의 이동 방향은, 인접한 칸 중 아무 냄새가 없는 방향으로 잡고, 그런 칸이 없으면 특정한 우선 순위 따른다
# : 우선순위는 상어마다 다르고, 같은 상어라도 방향에 따라 다를 수도 있다
# : 상어가 보고 있는 처음 방향은 입력으로, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다

# => 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다
# => 1번 상어만 남을 때까지 걸리는 초는?


n, m, k = map(int, input().split())

array = []
for i in range(n) :
    array.append(list(map(int, input().split())))

# 모든 상어, 현재 방향
directions = list(map(int, input().split()))

# 각 위치마다 [특정 냄새의 상어 번호, 특정 냄새의 남은 시간]
smell = [[[0, 0]] * n for _ in range(n)]

# 각 상어의 회전 방향 우선순위
priorities = [[] for _ in range(m)]
for i in range(m) :
    for j in range(4) :
        priorities[i].append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 모든 냄새
def update_smell() :
    for i in range(n) :
        for j in range(n) :
            # 냄새 존재하면 1 감소
            if smell[i][j][1] > 0 :
                smell[i][j][1] -= 1
            # 상어 존재하는 해당 위치 냄새를 k
            if array[i][j] != 0 :
                smell[i][j] = [array[i][j], k]

# 모든 상어 이동
def move() :
    new_array = [[0] * n for _ in range(n)]

    for x in range(n) :
        for y in range(n) :
            if array[x][y] != 0 :
                direction = direction[array[x][y] - 1]
                found = False
                # 냄새 존재하지 않는 곳 확인
                for index in range(4) :
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] -1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] -1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n :
                        if smell[nx][ny][0] == 0 : # 냄새 존재 x
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]
                        # 만약 있다면 번호 낮은 상어가
                        if new_array[nx][ny] == 0 :
                            new_array[nx][ny] = array[x][y]
                        else :
                            new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
                        found = True
                        break
                if found :
                    continue
                # 주변에 모두 있다면 자신 냄새로 이동
                for index in range(4) :
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] -1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] -1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n :
                        if smell[nx][ny][0]
 == array[x][y] : # 자신 냄새 있는 곳
                            # 해당 상어 방향 바꾸기
                            directions[array[x][y] - 1] = priorities[array[x][y]-1][direction -1][index]
                            # 상어 이동
                            new_array[nx][y] = array[x][y]
                            break
    retrun new_array

time = 0
while True :
    update_smell()
    new_array= move()
    array = new_array
    time += 1

    # 1번 상어
    check = True
    for i in range(n) :
        for j in range(n) :
            if array[i][j] > 1 :
                check = False
    if check :
        print(time)
        break

    if time >= 1000 :
        print(-1)
        break