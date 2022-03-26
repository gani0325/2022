# 숨바꼭질
# : 1 ~ N번까지의 헛간 중에서 하나를 골라 숨을 수 있으며, 술래는 항상 1번 헛간에서 출발
# : 전체 맵에는 총 M개의 양방향 통로가 존재, 하나의 통로는 서로 다른 두 헛간 연결
# : 전체 맵은 항상 어떤 헛간에서 다른 헛간으로 도달이 가능
# : 1번 헛간에서 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단
# : 최단 거리는 지나야 하는 길의 최소 개수
# : 동빈이가 숨을 헛간의 번호 출력

# : 다익스트라 알고리즘 사용하여 최단 거리 구하기

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n , m = map(int, input().split())
start = 1
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m) :
    a, b = map(int, input().split())
    # a, b 이동 비용이 1
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 최단 거리 가장 먼 노드
max_node = 0
# 최단 거리가 가장 먼 노드와의 최단 거리
max_distance = 0
# 동일한 최단 거리 리스트
result = []

for i in range(1, n+1) :
    if max_distance < distance[i] :
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i] :
        result.append(i)

print(max_node, max_distance, len(result))
