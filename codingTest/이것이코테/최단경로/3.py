# 3. 전보
# : 도시 c에서 받게 되는 도시의 개수는 몇 개이며, 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인가?
# : 도시 x에 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간 출력

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
# 노드, 간선, 시작 노드
n, m, start = map(int, input().split())
# 각 노드 연결되어 있는 노드에 대한 정보 담는 리스트
graph = [[] for i in range(n+1)]
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보
for _ in range(m) :
    x, y, z = map(int, input().split())
    # a 번 노드에서 b 번 노드로 가는 비용이 z
    graph[x].append((y, z))

def dijkstra(start) :
    q = []
    # 시작노드 가기위한 최단 경로는 0, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        # 현재 노드와 인접한 노드
        for i in graph[now] : 
            cost = dist + i[1]
            # 다른 노드 이동거리가 더 짧을 경우
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0

for d in distance :
    if d != INF :
        count += 1
        max_distance = max(max_distance, d)
# 시작노드 빼기
print(count - 1, max_distance)

# 3 2 1
# 1 2 4
# 1 3 2
# 2 4