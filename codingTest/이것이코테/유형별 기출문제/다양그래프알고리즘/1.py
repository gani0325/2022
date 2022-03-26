# 그래프 란
# : 노드와 노드 사이에 연결된 간선의 정보를 가지고 있는 자료구조
# - 인접 행렬 : 2차원 배열 사용
# - 인접 리스트 : 리스트 사용

# 1. 서로소 집합
# : 공통 원소가 없는 두 집합
# : 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# - union : 2개의 원소가 포함된 집합을 하나의 집합으로 합치기
# - find : 특정한 원소가 속한 집합이 어떤 집합인지 알려주기
# => union 연산을 하나씩 확인하면서 서로 다른 두 원소에 대해 합집합을 수행해야 할 때는, 각각 루트 노드를 찾아서 더 큰 루트 노드가 더 작은 루트 노드를 가리키도록 한다

# 기본적인 서로소 집합
def find_parent(parent, x) :
    # 루트 노드가 아니면, 찾을 때까지 재귀적 호출
    if parent[x] != x :
        return find_parent(parent, parent[x])
    return x

# 두 원소 속한 집합
def union_parent(paretn, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1) :
    parent[i] = i

for i in range(e) :
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("각 원소 속한 집합 : ", end = " ")
for i in range(1, v+1) :
    print(find_parent(parent, i), end = " ")

print()

print("부모 테이블 : ", end = " ")
for i in range(1, v+1) :
    print(parent[i], end = " ")

# 6 4
# 2 4
# 2 5
# 5 6
# 1 3
# 각 원소 속한 집합 :  1 2 1 2 2 2 
# 부모 테이블 :  1 2 1 2 2 2 




# 경로 압축
# def find_parent(parent, x) :
#     if parent[x] != x :
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# 2. 개선된 서로소 집합 알고리즘
def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두원소 속한 집합 합치기
def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)


for i in range(1, v+1) :
    parent[i] = i

for i in range(e) :
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소 속한 집합 출력
print("각 원소 속한 집합 : ", end = " ")
for i in range(1, v+1) :
    print(find_parent(parent, i), end = " ")

print()

print("부모 테이블 : ", end = " ")
for i in range(1, v+1) :
    print(parent[i], end = " ")

# 6 4
# 1 4
# 2 3
# 2 4
# 5 6
# 각 원소 속한 집합 :  1 1 1 1 5 5 
# 부모 테이블 :  1 1 1 1 5 5  



  
# 3. 서로소 집합을 활용한 사이드 판별
# : 각 간선 확인하며 두 노드의 루트노드 확인
# - 루트 노드가 다르면 union 연산
# - 루트 노드가 같다면 사이클 발생

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1) :
    parent[i] = i
cycle = False

for i in range(e) :
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b) :
        cycle = True  
        break
    else : 
        union_parent(parent, a, b)

if cycle :
    print("사이클 발생")
else :
    print("사이클 xxx")


# 3 3
# 1 2
# 2 3
# 1 3
# 사이클 발생




# 4. 신장 트리
# : 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

# 크루스칼 알고리즘
# : 가장 적은 비용으로 모든 노드르 ㄹ연결
# : 모든 간선에 대해 정렬 수행, 가장 거리가 짧은 간선부터 집합에 포함
# - 간선 데이터를 비용에 따라 오름차순
# - 간선 확인하며 현재 간선이 사이클 발생시키는지 확인
# (사이클 발생x 최소신장트리 포함, 사이클 발생o 최소신장트리 포함x)
# => 신장 트리 중에서 최소 비용으로 만들 수 있는 트리를 찾는 알고리즘
# => 가장 거리가 짧은 간선부터 차례대로 집합에 추가 (사이클 발생 간선 제외

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def unioin_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
v, e = map(int, input().split())
parent = [0]*(v+1)

edges = []
result = 0

for i in range(1, v+1) :
    parent[i] = i

for _ in range(e) :
    a, b, cost = map(int, input().split())
    # 비용순 정렬. 튜플의 첫번째 원소를 비용
    edges.append((cost, a, b))

edges.sort()

for edge in edges :
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b) :
        unioin_parent(parent, a, b)
        result += cost

print(result)


# 7 9 
# 1 2 79
# 1 3 78
# 1 5 66
# 2 4 89
# 2 5 34
# 4 3 12
# 5 6 23
# 6 7 12
# 7 4 15
# 162




# 위상 정렬
# : 순서가 정해져 있는 일련의 작업을 차례대로 수행할 때 사용
# : 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
# : 진입차수 (특정한 노드로 들어오는 간선의 개수)
# - 진입 차수가 0인 노드를 큐에 넣기
# - 큐기 빌 때까지 반복
# -- 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
# -- 새롭게 진입차수가 0이 된 노드를 큐에 넣음
# : O(V + E) 차례때로 모든 노드 확인 + 해당 노드에서 출발하는 간선 제거

from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보
for _ in range(e) :
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입차수 1 증가
    indegree[b] += 1

# 위상 정렬 함수  
def topology_sort() :
    result = []
    q = deque()  

    # 처음 시작할 때는 진입차수 0 노드를 큐에 삽입
    for i in range(1, v+1) :
        if indegree[i] == 0 :
            q.append(i)

    while q :
        now = q.popleft()
        result.append(now)

        for i in graph[now] :
            indegree[i] -= 1
            # 새롭게 진입차수 0인 노드 큐에 삽입
            if indegree[i] == 0 :
                q.append(i)
    for i in result :
        print(i, end= " ")

topology_sort()


# 7 8
# 1 2
# 1 5
# 2 3 
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
# 1 2 5 3 6 4 7  