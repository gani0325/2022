# 어른 상어

# 청소년 상어는 더욱 자라 어른 상어가 되었다.
# 상어가 사는 공간에 더 이상 물고기는 오지 않고 다른 상어들만이 남아있다. 
# 상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다. 
# 상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데,
    # 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.

# N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다. 
# 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다. 
# 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다. 
# 냄새는 상어가 k번 이동하고 나면 사라진다.

# 각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 
# 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 
# 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 
# 우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다. 
# 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.

# 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 
    # 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.

# 이 과정을 반복할 때, 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구하는 프로그램을 작성

# 첫 줄에는 N, M, k가 주어진다. (2 ≤ N ≤ 20, 2 ≤ M ≤ N2, 1 ≤ k ≤ 1,000)
# 그 다음 줄부터 N개의 줄에 걸쳐 격자의 모습이 주어진다.
    # 0은 빈칸이고, 0이 아닌 수 x는 x번 상어가 들어있는 칸을 의미한다.
# 그 다음 줄에는 각 상어의 방향이 차례대로 주어진다.
    # 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽을 의미한다.
# 그 다음 줄부터 각 상어의 방향 우선순위가 상어 당 4줄씩 차례대로 주어진다. 
    # 각 줄은 4개의 수로 이루어져 있다. 
        # 첫 번째 줄은 해당 상어가 위를 향할 때의 방향 우선순위,
        # 두 번째 줄은 아래를 향할 때의 우선순위, 
        # 세 번째 줄은 왼쪽을 향할 때의 우선순위, 
        # 네 번째 줄은 오른쪽을 향할 때의 우선순위
# 각 우선순위에는 1부터 4까지의 자연수가 한 번씩 나타난다. 가장 먼저 나오는 방향이 최우선
# 맨 처음에는 각 상어마다 인접한 빈 칸이 존재한다. 따라서 처음부터 이동을 못 하는 경우는 없다.

# 1번 상어만 격자에 남게 되기까지 걸리는 시간을 출력한다. 
# 단, 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력

# DFS
N, M, K = map(int, input().split())

# 처음 상어
data = []
for _ in range(N) :
    data.append(list(map(int, input().split())))

shark = [[0, 0] for _ in range(M)]

# 상어의 방향
directions = list(map(int, input().split()))
# 상어의 우선 순위
priority = []
for i in range(M) :
    temp = []
    for _ in range(4) :
        temp.append(list(map(int, input().split())))
    priority.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상어번호, 냄새 기간, 방향
smell = [[[0, 0]] * N for _ in range(N)]
def get_smell() :
    for i in range(N) :
        for j in range(M) :
            if smell[i][j][1] > 0 :
                smell[i][j][1] -= 1
            if data[i][j] != 0 :
                smell[i][j] = [data[i][j], K]
# 상어 이동
def dfs() :
    new_data = [[0] * N for _ in range(N)]
    for x in range(N) :
        for y in range(N) :
            if data[x][y] != 0 :
                direction = directions[data[x][y] - 1]
                found = False
                for idx in priority[data[x][y] - 1][direction - 1] :
                    nx = x + dx[idx - 1]
                    ny = y + dy[idx - 1]
                    if 0 <= nx < N and 0 <= ny < N :
                        if smell[nx][ny][1] == 0 :
                            directions[data[x][y] - 1] = idx
                            # 상어 이동하기
                            if new_data[nx][ny] == 0 :
                                new_data[nx][ny] == data[x][y]
                            else :
                                new_data[nx][ny] = min(data[x][y], new_data[nx][ny])
                            found = True
                            break
                if found :
                    continue
                
                # 모두 냄새 남아있으면, 자기 냄새로 이동
                for idx in priority[data[x][y] - 1][direction - 1] :
                    nx = x + dx[idx - 1]
                    ny = y + dy[idx - 1]
                    if 0 <= nx < N and 0 <= ny < N :
                        if smell[nx][ny][0] == data[x][y] :
                            directions[data[x][y] - 1] = idx
                            new_data[nx][ny] = data[x][y]
                            break
    return new_data

answer = 0
while True:
    get_smell()
    new_data = dfs()
    data = new_data
    answer += 1

    check = True
    for i in range(N):
        for j in range(N):
            if data[i][j] > 1:
                check = False
    if check:
        print(answer)
        break

    # 1000초가 지날 때까지 끝나지 않음
    if answer >= 1000:
        print(-1)
        break