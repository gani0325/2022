# DFS
# 스택 자료 구조 이용 (재귀도 가능)
# - 탐색 시작 노드를 스택에 삽입하고 방문 처리
# - 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면, 그 인접 노드를 스택에 넣고 방문 처리 한다 ( 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드 꺼낸다 )
# - 2번 과정을 더이상 수행할 수 없을 때까지 반복
# 방문처리란 : 스택에 한 번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크하는 것
# 데이터 개수가 N 개 이면 O(N)

def dfs(graph, v, visited) :
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드 방문
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

graph = [
  [],
  [3, 5, 6],
  [1, 4, 6],
  [1, 5],
  [2, 3, 4],
  [3, 4],
  [6],
  [2, 5]
]

visited = [False] * 8

dfs(graph, 1, visited)






# BFS Breath Frist Search
# : 너비 우선 탐색
# : 가까운 노드부터 탐색하는 알고리즘
# : 선입선출 방식인 큐 자료 구조 이용
# - 탐색 시작 노드를 큐에 삽입하고 방문 처리 한다
# - 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
# - 2번 과정 더이상 수행할 수 없을 때가지 반복
# O(N) 소요

from collections import deque

def bfs(graph, start, visited) :
    queue = deque([start])
    # 방문 처리
    visited[start] = True
    # 큐 빌 때까지 반복
    while queue :
        v = queue.popleft()
        print(v, end = " ")

        # 해당 원소와 연결된, 방문하지 않은 원소 큐에 삽입
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

graph = [
  [],
  [3, 5, 6],
  [1, 4, 6],
  [1, 5],
  [2, 3, 4],
  [3, 4],
  [6],
  [2, 5]
]

visited = [False] * 8

bfs(graph, 1, visited)


# DFS : 스택 + 재귀 함수
# BFS : 큐