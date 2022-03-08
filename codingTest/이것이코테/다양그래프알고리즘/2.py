# 팀 결성
# : 0 ~ N번의 N+1 팀 존재
# - 팁 합치기 연산은 두 팀 합치기 (0, a, b)
# - 같은 팀 여부 확인은 특정한 두 학생이 같은 팀에 속하는지 (1, a, b)

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, x)
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(0, n+1) :
    parent[i] = i

for i in range(m) :
    oper, a, b= map(int, input().split())
    # 합집합
    if oper == 0 :
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b) :
            print("YES")
        else :
            print("NO")

# 7 6
# 0 1 2
# 1 3 4
# NO
# 1 5 6
# NO
# 0 5 6