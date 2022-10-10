# 연구소

# 인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출
# 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다

# 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다
# 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 

# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

# 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다.
# 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

# 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역
# 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성

# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
# 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다.
#     0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치
#     2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수
# 빈 칸의 개수는 3개 이상이다.

# 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력

# 1) DFS
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for i in range(N) :
    graph.append(list(map(int, input().split())))
temp = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

# 바이러스 퍼지기
def virus(x, y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M :
            if temp[nx][ny] == 0 :      # 빈칸
                temp[nx][ny] = 2        # 바이러스 퍼짐
                virus(nx, ny)
    return

# 안전영역 크기 계산
def score() :
    score = 0
    for i in range(N) :
        for j in range(M) :
            if temp[i][j] == 0 :
                score += 1
    return score

# DFS 이용해서 벽 설치
def dfs(cnt) : 
    global result
    if cnt == 3 :
        for i in range(N) :
            for j in range(M) :
                temp[i][j] = graph[i][j]

        for i in range(N) :
            for j in range(M) :
                if temp[i][j] == 2 :        # 바이러스라면!
                    virus(i, j)             # 퍼져라! 
        result = max(result, score())
        return
    
    # 벽 세우기. 경우의 수 탐색
    for i in range(N) :
        for j in range(M) :
            if graph[i][j] == 0 :
                graph[i][j] = 1        # 벽 세워요
                cnt += 1                # 벽 개수 증가
                dfs(cnt)
                graph[i][j] = 0         # 최적의 경우의 수가 아니면 초기화
                cnt -= 1  
dfs(0)
print(result)

# input
# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

# output
# 27