# 나무 재테크

# 각각의 칸은 (r, c)
# 가장 처음에 양분은 모든 칸에 5만큼 들어있다.

# 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
# 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다.
# 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
# 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.

# 여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
# 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다.
# 소수점 아래는 버린다.

# 가을에는 나무가 번식한다.
# 번식하는 나무는 나이가 5의 배수이어야 하며,
# 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
# 어떤 칸 (r, c)와 인접한 칸은
# (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다.
# 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.

# 겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다.
# 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.

# K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성

from collections import deque

n, m, k = map(int, input().split())

arr = [[5] * n for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)]

# S2D2 A배열의 값
S2D2 = []
for i in range(n) :
    S2D2.append(list(map(int, input().split())))

# 나무의 정보를 나타내는 세 정수 x, y, z (위치 x,y  나무의 나이 z)
for i in range(m) :
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

while k > 0 :
    # 봄
    for i in range(n) :
        for j in range(n) :
            t_len = len(tree[i][j])
            for q in range(t_len) :
                if arr[i][j] >= tree[i][j][q] :
                    arr[i][j] -= tree[i][j][q]
                    tree[i][j][q] += 1
                else :
                    # 여름
                    for _ in range(q, t_len) :
                        arr[i][j] += tree[i][j].pop() // 2
                    break
    # 가을
    for i in range(n) :
        for j in range(n) :
            for e in tree[i][j] :
                if e % 5 == 0 :
                    for h in range(8):
                        nx = i + dx[h]
                        ny = j + dy[h]
                        if 0 <= nx < n and 0 <= ny < n :
                            tree[nx][ny].appendleft(1)
            # 겨울
            arr[i][j] += S2D2[i][j]
    k -= 1

result = 0
for i in range(n) :
    for j in range(n) :
        result += len(tree[i][j])
print(result)
