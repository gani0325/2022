# 사다리 조작

# 사다리 게임은 N개의 세로선과 M개의 가로선으로 이루어져 있다. 
# 인접한 세로선 사이에는 가로선을 놓을 수 있는데, 
# 각각의 세로선마다 가로선을 놓을 수 있는 위치의 개수는 H이고, 모든 세로선이 같은 위치를 갖는다

# 초록선은 세로선을 나타내고, 초록선과 점선이 교차하는 점은 가로선을 놓을 수 있는 점
# 가로선은 인접한 두 세로선을 연결해야 한다. 
# 단, 두 가로선이 연속하거나 서로 접하면 안 된다. 또, 가로선은 점선 위에 있어야 한다.

# 가로선은 위의 그림과 같이 인접한 두 세로선을 연결해야 하고, 가로선을 놓을 수 있는 위치를 연결해야 한다.
# 사다리 게임은 각각의 세로선마다 게임을 진행하고, 세로선의 가장 위에서부터 아래 방향으로 내려가야 한다. 
# 이때, 가로선을 만나면 가로선을 이용해 옆 세로선으로 이동한 다음, 이동한 세로선에서 아래 방향으로 이동해야 한다.

# 사다리에 가로선을 추가해서, 사다리 게임의 결과를 조작하려고 한다.
# 이때, i번 세로선의 결과가 i번이 나와야 한다.
# 추가해야 하는 가로선 개수의 최솟값을 구하는 프로그램을 작성

# 첫째 줄에 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수 H가 주어진다. (2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H)
# 둘째 줄부터 M개의 줄에는 가로선의 정보가 한 줄에 하나씩 주어진다.
#     가로선의 정보는 두 정수 a과 b로 나타낸다. (1 ≤ a ≤ H, 1 ≤ b ≤ N-1) 
#     b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미
# 가장 위에 있는 점선의 번호는 1번이고, 아래로 내려갈 때마다 1이 증가
#     세로선은 가장 왼쪽에 있는 것의 번호가 1번이고, 오른쪽으로 갈 때마다 1이 증가한다.
# 입력으로 주어지는 가로선이 서로 연속하는 경우는 없다

# i번 세로선의 결과가 i번이 나오도록 사다리 게임을 조작하려면, 추가해야 하는 가로선 개수의 최솟값을 출력
#     만약, 정답이 3보다 큰 값이면 -1을 출력한다. 또, 불가능한 경우에도 -1을 출력한다.

def check() :
    for i in range(N) :     # 세로선 검사
        k = i   # 이동하는 가로선
        for j in range(H) :
            if visited[j][k] :     # 가로선 존재 -> 오른쪽
                k += 1
            elif k > 0 and visited[j][k-1] :       # 가로선 왼쪽에 존재 -> 왼쪽으로
                k -= 1
        if k != i :
            return False
    return True

def dfs(cnt, x, y ) :
    global answer
    if check() :
        answer = min(answer, cnt)
        return
    
    elif cnt == 3 or answer <= cnt :
        return

    for i in range(x, H) :
        # 행 탐색
        if i == x :
            k = y
        else :
            k = 0

        for j in range(k, N - 1):
            # 열 탐색
            if not visited[i][j] and not visited[i][j+1] :
                if j > 0 and visited[i][j - 1] :
                    continue
            
                visited[i][j] = True
                dfs(cnt+1, i, j +2)
                visited[i][j] = False

# 세로선 개수, 가로선 개수, 세로선 마다 가로선 놓을 수 있는 위치개수
N, M, H = map(int, input().split())    

visited = [[False] * N for _ in range(H)]       # 방문 확인

if M == 0 :  # 가로선 없음
    print(0)    # 최소값 0
    exit(0)

for _ in range(M) :
    a, b = map(int, input().split())    # 가로선 정보
    visited[a-1][b-1] = True
answer = 4

dfs(0, 0, 0)

if answer < 4 :
    print(answer)
else :
    print(-1)