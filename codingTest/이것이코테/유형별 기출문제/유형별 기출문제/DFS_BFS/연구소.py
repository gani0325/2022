# 연구소
# : 크기가 N X M 직사각형
# : 1 X 1 크기의 정사각형으로 나눠짐
# : 빈칸, 벽으로 이루어져 벽은 칸 하나를 가득 차지
# : 일부 칸은 바이러스 존재, 상하좌우로 인접한 빈칸으로 모두 퍼져나감
# : 새로 세울 수 있는 벽의 개수는 3개이며 꼭 3개 세워야 한다
# : 0은 빈칸, 1은 벽, 2는 바이러스
# : 바이러스가 퍼질 수 없는 곳을 안전영역일 때 최대값 구하라

n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n) :
    data.append(list(map(int, input().split())))

dx = [-1 , 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

# DFS virus difusal
def virus(x, y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m :
            if temp[nx][ny] == 0 :
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n) :
        for j in range(m) :
            if temp[i][j] == 0:
                score += 1
    return score

# DFS safe space 
def dfs(count) :
    global result
    if count == 3 :
        for i in range(n) :
            for j in range(m) :
                temp[i][j] = data[i][j]

        for i in range(n) :
            for j in range(m) :
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return
    for i in range(n) :
        for j in range(m) :
            if data[i][j] == 0 :
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)