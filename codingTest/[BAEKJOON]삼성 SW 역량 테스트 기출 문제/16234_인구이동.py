# 인구 이동

# r행 c열에 있는 나라에는 A[r][c]명이 살고 있다.
# 인접한 나라 사이에는 국경선이 존재

# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면,
# 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.

# 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면,
# 그 나라를 오늘 하루 동안은 연합이라고 한다.

# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가
# 편의상 소수점은 버린다.

# 연합을 해체하고, 모든 국경선을 닫는다.

# 각 나라의 인구수가 주어졌을 때,
# 인구 이동이 며칠 동안 발생하는지 구하는 프로그램

from collections import deque

N, L, R = map(int, input().split())
#people = (list(map(int, input().split())) for _ in range(N))
people = []
for _ in range(N) :
    people.append(list(map(int ,input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

def process(x, y, index) :
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = people[x][y]
    count = 1

    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1 :
                if L <= abs(people[nx][ny] - people[x][y]) <= R :
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += people[nx][ny]
                    count += 1
                    united.append((nx, ny))

    for i, j in united :
        people[i][j] = summary // count
    return count

total_count = 0

while True :
    union = [[-1] * N for _ in range(N)]
    index = 0
    for i in range(N) :
        for j in range(N) :
            if union[i][j] == -1 :
                process(i, j, index)
                index += 1
    if index == N*N :
        break
    total_count += 1
print(total_count)