# 최단 경로 : 가장 짧은 경로 찾기
# 1. 다익스트라 최단 경로
# : 여러 개의 노드가 있을 떄, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
# - 출발 노드 설정
# - 최단 거리 테이블 초기화
# - 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
# - 해당 노드를 거쳐 다른 노드로 가는 비용 계산, 최단 거리 테이블 갱신
# - 3,4 번 반복
# => 구현하기 쉽지만 느리게 동작하는 코드
# => 구현하기에 조금 더 까다롭지만 빠르게 동작하는 코드
# : O(V^2)의 시간 복잡도 (V 는 노드의 개수)
# : 단계마다 "방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택" 하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색)


# 간단한 다익스트라 알고리즘
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한 의미

# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())
# 각 노드에 연결되어있는 노드 정보 리스트
graph = [[] for i in range(n+1)]
# 방문 체크 리스트
visited = [False] * (n+1)
# 최단 거리 테이블 모두 초기화
distance = [INF] * (n+1)

# 모든 간선 정보
for _ in range(m) :
    a, b, c = map(int, input().split()) # a 에서 b 로 가는 비용이 c
    graph[a].append((b,c))

# 방문 하지 않은 노드 중, 가장 최단 거리 짧은 노드 번호
def get_smallest_node() :
    min_value = INF
    index = 0 # 가장 최단 거리 짧은 노드
    for i in range(1, n+1) :
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index = i
    return index

def dijkstra(start) :
    distance[start] = 0
    visited[start] = True
    for j in graph[start] :
        distance[j[0]] = j[1]

    for i in range(n-1) :
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now] :
            cost = distance[now] + j[1]
            if cost < distance[j[0]] :
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print("infinity")
    else :
        print(distance[i])

# 6 11
# 1
# 1 2 2
# 1 3 5 
# 1 4 1
# 2 3 3
# 2 4 2 
# 3 2 3
# 3 6 5
# 4 5 5
# 4 5 1
# 3 4 1
# 4 6 2
# 0
# 2
# 5
# 1
# 2
# 3




# 개선된 다익스트라 알고리즘
# : 힙 구조 사용
# : 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아 처리
# : 힙은 우선순위 큐를 구현하기 위함, 운선순위가 가장 높은 데이터를 먼저 삭제
# + 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐 사용

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한 의미

# 노드, 간선 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())
# 각 노드에 연결되어 있는 노드 정보 리스트
graph = [[] for i in range(n+1)]
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q :  # 큐 비어있지 않다면
        # 가장 최단 거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 이미 처리되면 무시
        if distance[now] < dist :
            continue
        # 다른 인접 노드 확인 
        for i in graph[now] :
            cost = dist + i[1]
            # 다른 노드가 더 짧다면?
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print("infinity")
    else :
        print(distance[i])

# 6 11 
# 1
# 1 2 2
# 1 3 5 
# 2 4 3
# 2 5 6 
# 3 4 4
# 5 4 3
# 3 2 5
# 5 6 4
# 6 5 1
# 6 3 4
# 3 5 6
# 0
# 2
# 5
# 5
# 8
# 12
        




# 플로이드 워셜 알고리즈
# : 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
# : 단계마다 거쳐가는 노드 기준
# : 총 시간 복잡도는 O(N^3)
# => A에서 B로 가는 최소 비용과 A에서 K를 거쳐 B로 가는 비용 을 비교하여 더 작은 값으로 갱신

INF = int(1e9)

# 노드, 간선 개수
n = int(input())
m = int(input())

# 2차원 리스트 + 모든 값 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신 -> 자기자신 0으로 초기화
for a in range(1, n+1) :
    for b in range(1, n+1) :
        if a == b :
            graph[a][b] = 0
# 각 간선 정보 -> 그 값으로 초기화
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘
for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n+1) :
    for b in range(1, n+1) :
        if graph[a][b] == INF :
            print("infinity")
        else :
            print(graph[a][b], end = " ")
    print()



# 4
# 7
# 1 2 4
# 1 3 5
# 2 1 3
# 2 3 7
# 3 2 5
# 3 4 4
# 4 3 2
# 0 4 5 9 
# 3 0 7 11 
# 8 5 0 4 
# 10 7 2 0 