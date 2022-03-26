# 탑승구
# : G개의 탑승구가 있음 1번부터 G번까지의 번호
# : P 개의 비행기가 차례대로 도착할 예정
# : i번째 비행기를 1번부터 g번째 탑승구 중 하나에 영구적으로 도킹 ( 다른 비행기가 도킹하지 않은 탑승구에만 도킹 가능)
# : P개의 비행기를 순서대로 도킹하다가, 어떠한 탑승구에도 도킹할 수 없다면 공항 운행 중지!
# : 최대한 많은 비행기를 공항에 도킹!
# : 최대 몇 대 도킹 가능?

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else : 
        parent[a] = b
# 탑승구 개수
g = int(input())

# 비행기 개수
p = int(input())

parent = [0] * (g+1)
for i in range(1, g+1) :
    parent[i] = i

result = 0
for _ in range(p) :
    data = find_parent(parent, int(input())) # 현재 비행기 탑승구 루트 확인
    if data == 0 : # 루트 0이면
        break
    union_parent(parent, data, data - 1) # 왼쪽 집합과 합치기
    result += 1

print(result)