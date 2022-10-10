# 테트로미노

# 폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형
#     정사각형은 서로 겹치면 안 된다.
#     도형은 모두 연결되어 있어야 한다.
#     정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
#     정사각형 4개를 이어 붙인 폴리오미노는 테트로미노

# 아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 
# 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.

# 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성
# 테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

# 첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)
# 둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. 
# i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수
# 입력으로 주어지는 수는 1,000을 넘지 않는 자연수

# 첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.

# 1) DFS
N, M = map(int, input().split())
graph = []
for i in range(N) :
    graph.append(list(map(int, input().split())))

max_val = max(map(max, graph))
visited = [[False] * M for _ in range(N)]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
result = 0

def dfs(x, y, step, total) :
    global result
    
    # 최대값 못 넘기면 종료
    if total + max_val * (4 - step) <= result :
        return
    
    # 블록 4개 다쓰면 종료
    if step == 4 :
        result = max(result, total)
        return

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위내 있고, 방문하지 않았다면
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] :
            # 블록 연결 후 ㅏ, ㅓ, ㅗ, ㅜ 모양 만들기
            if step == 2 :
                visited[nx][ny] = True      # 탐색함
                dfs(x, y, step + 1, total+graph[nx][ny])
                visited[nx][ny] = False     # 탐색 제거

            visited[nx][ny] = True
            dfs(nx, ny, step + 1, total+graph[nx][ny])
            visited[nx][ny] = False



for i in range(N) :
    for j in range(M) :
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = False
print(result)

# input
# 5 5
# 1 2 3 4 5
# 5 4 3 2 1
# 2 3 4 5 6
# 6 5 4 3 2
# 1 2 1 2 1

# output
# 19