# 행성 터널
# : 왕국은 N개의 행성으로 이루어짐
# : 효율적으로 지배하기 위해 연결된 터널 만들기로 함
# : 행성은 3차원 좌표 위의 한 점!
# : 터널을 총 N-1 개 건설해서 모든 행성이 서로 연결되게 한다
# : 모든 행성을 터널로 연결하는데 필요한 최소 비용 구하라

# => 크루스칼 알고리즘

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

n = int(input())
parent = [0]  * (n+1)

# 부모 자기자신으로 초기화
for i in range(1, n+1) :
    parent[i] = i

edges = []
result = 0

x = []
y = []
z = []

# 모든 노드에 대한 좌표 값
for i in range(1, n+1) :
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

# 인접한 노들들로부터 간선 정보 추출 처리
for i in range(n-1) :
    # 비용순 정렬
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort()

# 간선 확인
for edge in edges : 
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        result += cost

print(result)