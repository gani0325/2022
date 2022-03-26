# 치킨 배달
# : N X N 도시에 1 X 1 칸으로 나뉨
# : 빈칸, 치킨집, 집 중 하나
# : 도시의 칸은 (r, x) 위에서 r칸, 왼쪽에서 c칸 (1부터 시작)
# : 치킨거리는 집과 가장 가까운 치킨집 사이의 거리
# : 각각의 집은 치킨 거리 가짐
# : 도시의치킨 거리는 모든 집의 치킨 거리 합이다
# : 도시에 있는 치킨집 중 최대 M개 고르고, 나머지는 폐업
# : 어떻게 고르면, 도시의 치킨 거리가 가장 작게 되나?

from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n) :
    data = list(map(int, input().split()))
    for c in range(n) :
        if data[c] == 1:
            house.append((r, c))   # 일반 집
        elif data[c] == 2 :
            chicken.append((r, c))   # 치킨 집

# 모든 치킨집 중 m개의 치킨집 뽑는 조합
candidates = list(combinations(chicken, m))

# 치킨 거리 합
def get_sum(candidate) :
    result = 0
    for hx, hy in house :
        temp = 1e9
        for cx, cy in candidate :
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

result = 1e9
for candidate in candidates :
    result = min(result, get_sum(candidate))

print(result)