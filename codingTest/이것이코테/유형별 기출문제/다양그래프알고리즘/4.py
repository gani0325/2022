# 커리큘럼
# : N개의 강의를 들어야함. 동시에 여러개 강의 듣기 가능
# : 듣고자 하는 N개의 강의 정보가 주어졌을 때, N개의 강의에 대해 수강하기까지 걸리는 최소 시간 출력

from collections import deque
import copy

# 노드의 개수
v = int(input())
# 모든 노드 진입차수는 0
indegree = [0] * (v+1)
graph =[[] for i in range(v+1)]
# 각 강의 시간 0
time = [0] * (v+1)

# 방향 그래프의 모든 간선 정보
for i in range(1, v+1) :
    data = list(map(int, input().split()))
    time[i] = data[0]  # 첫번째 수는 시간 정보
    for x in data[1:-1] :
        indegree[i] += 1
        graph[x].append(i)

def topology_sort() :
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1) :
        if indegree[i] == 0 :
            q.append(i)

    while q :
        now = q.popleft()
        for i in graph[now] :
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0 :
                q.append(i)

    for i in range(1, v+1) :
        print(result[i])

topology_sort()


# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1
# 10
# 20
# 14
# 18
# 17