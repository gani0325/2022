# 특정거리의 도시 찾기
# : 1~N번까지으 ㅣ도시와 M개의 단방향 도로가 존재 (모든 도로의 거리는 1)
# : 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램은?

# - 도시의 개수 N
# - 도로의 개수 M
# - 거리 정보 K
# - 출발 도시의 번호 X
# : 모든 도로의 거리는 1라서, 너비 우선 탐색 이용 (BFS)

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 모든 도로 정보입력
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)

    # 모든 도시에 대한 최단 거리 초기화
    distance = [-1] * (n+1)
    distance[x] = 0

    # BFS
    q = deque([x])
    while q :
        now = q.popleft()
        for next_node in graph[now] :
            if distance[next_node] == -1 :
                distance[next_node] = distance[now] + 1
                q.append(next_node)

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1) :
    if distance[i] == k :
        print(i)
        check = True

if check == False :
    print(-1)

