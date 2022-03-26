# 도시 분할 계획
# : 마을은 N개의 집, 그 집을 연결하는 M개의 길
# : 임의의 두 집 사이에 경로는 항상 존재, 마을에는 집이 하나 이상 있기
# : 첫 째 줄의 길을 없애고 나머지 길의 유지비 합을 최소로 하기

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, x)
    return parent[x]

def union_paret(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

# 모든 간선 담을 리스트, 최종 비용 담을 변수
edges = []
result = 0

for i in range(v+1) :
    parent[i] = i

for _ in range(e) :
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0  # 가장 비용 큰 간선

for edge in edges :
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b) :
        union_paret(parent, a, b)
        result += cost
        last = cost
print(result - cost)


