# 감시
# 사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램
# 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호


import copy

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]],
             [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]

def watch(y, x, direction, tmp):
    for d in direction:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx >= 0 and nx < m and ny >= 0 and ny < n and tmp[ny][nx] != 6:
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = '#'
            else:
                break

def dfs(office, cnt):
    global ans

    tmp = copy.deepcopy(office)
    if cnt == cctv_cnt:
        c = 0
        for i in tmp:
            c += i.count(0)
        ans = min(ans, c)
        return
    y, x, cctv = q[cnt]
    for i in direction[cctv]:
        watch(y, x, i, tmp)
        dfs(tmp, cnt + 1)
        tmp = copy.deepcopy(office)

n, m = map(int ,input().split())
office =[]
cctv_cnt = 0
q = []
ans = int(1e9)
for i in range(n) :
    input_data = list(map(int, input().split()))
    office.append(input_data)
    for j in range(len(input_data)):
        if input_data[j] != 0 and input_data[j] != 6 :
            cctv_cnt += 1
            q.append([i, j, input_data[j]])

dfs(office, 0)
print(ans)