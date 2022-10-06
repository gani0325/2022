# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향

from collections import deque

n, m, v = map(int, input().split())

# 1. graph와 visited 리스트
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

# 2, grahp에 간선 노드 추가
for _ in range(m):  # m은 간선 개수
    x, y = map(int, input().split())
    graph[x][y] = 1  # 선이 양방향이기 때문에 x->y y->x 둘다 가는 거로 생각
    graph[y][x] = 1


def dfs(graph, v):
    visited[v] = True  # 탐색 시작 정점이 v
    print(v, end=" ")

    for i in range(len(graph[v])):
        if graph[v][i] == 1 and visited[i] == False:
            dfs(graph, i)


def bfs(graph, v):
    queue = deque([v])

    visited = [False] * (n + 1)  #  초기화
    visited[v] = True  # 탐색 시작 정점이 v

    while queue:  # 큐 값 있을 때까지
        v = queue.popleft()  # 방문한 노드 pop! 앞 요소 제거
        print(v, end=" ")

        for i in range(len(graph[v])):
            if graph[v][i] == 1 and visited[i] == False:  # i 다녀갔고 노드 값 1
                queue.append(i)
                visited[i] = True
    return visited


dfs(graph, v)
print()
bfs(graph, v)

# input
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# output
# 1 2 4 3
# 1 2 3 4
