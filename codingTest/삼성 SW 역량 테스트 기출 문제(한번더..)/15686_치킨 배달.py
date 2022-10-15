# 치킨 배달

# 크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다. 
# 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 
# 도시의 칸은 (r, c)와 같은 형태로 나타내고, 
# r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작

# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 
# 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다.
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다

# 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.
# 0은 빈 칸, 1은 집, 2는 치킨집이다.

# 이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다.
# 프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 한다. 
# 오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개

# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다.
#  어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성

# 첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.
# 둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.
# 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미
#     집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재
#     치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

# 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력

from itertools import combinations

N, M = map(int, input().split())

# 조합으로 M개 뽑고, 각각 치킨 거리 구하고, 도시의 치킨거리를 최솟값 계속 갱신
city = []
for i in range(N) :
    # 0은 빈 칸, 1은 집, 2는 치킨집
    city.append(list(map(int, input().split())))
house = []
chicken = []

for i in range(N) :
    for j in range(N) :
        # 집이면
        if city[i][j] == 1 :
            house.append([i, j])
        # 치킨집이면
        elif city[i][j] == 2 :
            chicken.append([i, j])

# 치킨집을 M개 선택했을 때
combi = list(combinations(chicken, M))
result = []

for com in combi :
    answer = 0
    for h in house :
        x1, y1 = h
        dist = int(1e9)
        for c in com :
            x2, y2 = c
            dist = min(dist, abs(x1-x2) + abs(y1-y2))
        answer += dist 
    result.append(answer)

print(min(result))