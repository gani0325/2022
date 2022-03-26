# 최종 순위
# : 총 n개의 팀 참가
# : 팀은 1번부터 n번까지 번호가 매김
# : 작년 순위와 상대적인 순위가 바뀐 모든 팀의 목록이 주어졌을 때, 올해 순위를 만들어라
# : 확실하지 않을수도, 일관성이 없는 잘못된 정보일 수 도 있음
# : 정해진 우선순위에 맞게 전체 팀들의 순서를 나열
# : 위상 정렬 알고리즘
# = > 자기보다 낮은 등수를 가진 팀을 가리키도록 방향 그래프 만들다

from collections import deque

for tc in range(int(input())) :
    n = int(input())
    indegree = [0] * (n+1)
    graph = [[False]  * (n+1) for i in range(n+1)]

# 작년 순위
data = list(map(int, input().split()))
# 초기화
for i in range(n) :
    for j in range(i+1, n) :
        graph[data[i]][data[j]] = True
        indegree[data[j]] += 1
# 올해 정보
m = int(input())
for i in range(m) :
    a, b = map(int, input().split())
    # 간선 방향 뒤집기
    if graph[a][b] :
        graph[a][b] = False
        graph[b][a] = True
        indegree[a] += 1
        indegree[b] -= 1
    else : 
        graph[a][b] = True
        graph[b][a] = False
        indegree[a] -= 1
        indegree[b] += 1


# 위상 알고리즘
result = []
q = deque()

for i in range(1, n+1) :
    if indegree[i] == 0 :
        q.append(i)

certain = True
cycle = False

for i in range(n) :
    if len(q) == 0 :
        cycle = True
        break
    if len(q) >= 2 :
        certain = False
        break
    now = q.popleft()
    result.append(now)
    for i in range(1, n+1) :
        if graph[now][i] :
            indegree[i] -= 1
            if indegree[i] ==0 :
                q.append(i)

if cycle :
    print("불가능")
elif not certain :
    print("?")
else :
    for i in result :
        print(i, end = " ")
    print()