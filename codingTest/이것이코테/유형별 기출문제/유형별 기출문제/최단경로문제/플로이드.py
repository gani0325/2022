# 플로이드
# : n(1<= n <= 100)개의 도시가 있고, 한 도시에 출발하여 다른 도시에 도착하는 m(1 <= m <= 100,000) 개의 버스가 있음
# : 각 버스는 한번 사용할 때 필요한 비용 있음
# : 모든 도시의 쌍(A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최소값을 구하라

# : 최단경로 알고리즘은 가장 짧은 경로를 찾는 것
# - 다익스트라 : 한 지점에서 다른 모든 지점까지의 최단 경로 계산 (우선순위 큐 이용)
# - 플로이드 워셜 : 모든 지점에서 다른 모든 지점까지의 최단 경로 계산 (점화식!!)

INF = int(1e9) # 무한 의미

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기에서 자기로 가는 비용은 0
for a in range(1, n+1) :
    for b in range(1, n+1) :
        if a == b:
            graph[a][b] = 0

# 각 간선 정보 받고 초기화
for _ in range(m) :
    a, b, c = map(int, input().split())
    # 가장 짧은 경로
    if c < graph[a][b] :
        graph[a][b] = c

for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1) :
    for b in range(1, n+1) :
        if graph[a][b] == INF :
            print(0, end = " ")
        else :
            print(graph[a][b], end = " ")

    print()