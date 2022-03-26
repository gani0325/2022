# 어두운 길
# : N개의 집과 M개의 도로가 구성
# : 각 집은 0부터 N-1번까지의 번호로 구분
# : 모든 도로에는 가로등이 구비, 특정한 도로의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와 동일
# : 일부 가로등을 비활성화하되, 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 함
# : 마을의 집과 도로 정보가 주어졌을 때, 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하라
# => 최소 신장 트리!! 각 노드가 서로 연결되어있다
# =< 크루스칼 알고리즘!!

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

# 모든 간선 담은 리스트, 최종 비용
edges = []
result = 0

# 부모 자기자신으로 초기화
for i in range(1, n+1) :
    parent[i] = i

for _ in range(1, n+1) :
    x, y, z = map(int, input().split())
    # 비용순 정렬
    edges.append((z, x, y))

edges.sort()
total = 0 # 전체 가로등 비용

for edge in edges :
    cost, a, b = edge
    total += cost
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        result += cost
print(total - result)