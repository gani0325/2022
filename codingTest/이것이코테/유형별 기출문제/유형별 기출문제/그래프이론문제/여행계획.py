# 서로소 집합 알고리즘 : 공통 원소가 없음 (재귀적)
# 신장 트리 : 하나의 그래프가 있을 때 모든 노드를 포함하는 부분 그래프
# : 크루스칼 알고리즘 : 가능한 최소 비용의 신장 트리 찾아주기 (간선의 비용이 작은 순서대로 만든다)
# : 위상 정렬 알고리즘 : 방향 그래프의 모든 노드들을 방향성에 거스리지 않도록 순서대로 나열하는 정렬 기법


# 여행 계획
# : N개의 여행지가 있고 1~N개의 번호로 구분
# : 임의의 두 여행지 사이에는 두 여행지를 연결하는 도로가 존재
# : 도로로 연결되어 있따면 양방향 이동 가능
# : 여행 계획이 가능한지 여부 판단하자
# : 1이 연결, 0은 연결 X
# => 여행 계획에 해당하는 모든 노드가 같은 집합에 속하기만 하면 가능하 ㄴ여행 경로!! (union 연산 이용해서 같은 집합에 속하도록!)
# : 서로소 집합 이용하여 함

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소 속한 집합
def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().split())
parent = [0]  * (n+1)

# 부모 자기자신으로 초기화
for i in range(1, n+1) :
    parent[i] = i

# union 연산
for i in range(n) :
    data = list(map(int, input().split()))
    for j in range(n) :
        if data[j] == 1 : #연결!!
            union_parent(parent, i+1, j+1)

# 여행 계획
plan = list(map(int, input().split()))

result = True
# 모든 노드의 루트가 동일한가
for i in range(m - 1) :
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]) :
        result = False

if result :
    print("YES")
else : 
    print("NO")