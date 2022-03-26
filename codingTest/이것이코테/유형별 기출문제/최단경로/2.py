# 2. 미래도시
# : 방문 판매원이 회사를 이동하게 되는 최소 시간계산
# : A가 K번 회사를 거쳐서 X번 회사로 가는 최소 이동 시간은?

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신으로 초기화
for a in range(1, n+1) :
    for b in range(1, n+1) :
        if a == b:
            graph[a][b] = 0

# 각 간선 정보 입력, 초기화
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 x, 최종 목적지 k
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF :
    print("-1")
else :
    print(distance)

# 4 2
# 1 3
# 2 4
# 3 4
# -1