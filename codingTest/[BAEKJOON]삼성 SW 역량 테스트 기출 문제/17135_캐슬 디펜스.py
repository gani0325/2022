# 캐슬 디펜스

# 격자판의 N번행의 바로 아래(N+1번 행)의 모든 칸에는 성이 있다.

# 성을 적에게서 지키기 위해 궁수 3명을 배치하려고 한다.
# 궁수는 성이 있는 칸에 배치할 수 있고, 하나의 칸에는 최대 1명의 궁수만 있을 수 있다.
# 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다.

# 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고,
# 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다.
# 같은 적이 여러 궁수에게 공격당할 수 있다. 공격받은 적은 게임에서 제외된다.

# 궁수의 공격이 끝나면, 적이 이동한다.
# 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다.

# 모든 적이 격자판에서 제외되면 게임이 끝난다.

# 이 게임은 궁수의 위치가 중요하다. 격자판의 상태가 주어졌을 때,
# 궁수의 공격으로 제거할 수 있는 적의 최대 수를 계산해보자.

# 격자판의 두 위치 (r1, c1), (r2, c2)의 거리는 |r1-r2| + |c1-c2|이다.

# 0은 빈 칸, 1은 적이 있는 칸

import copy

def combinations(array, r):
    for i in range(len(array)):
        if r == 1:  # 종료 조건
            yield [array[i]]
        else:
            for next in combinations(array[i + 1:], r - 1):
                yield [array[i]] + next

def attack(list_):
    attack_list = list()
    cnt = 0
    for l in list_ :
        pos = list()
        for i in range(n) :
            for j in range(m) :
                if temp[i][j] == 1 :
                    now_d = abs(i - n) + abs(j - l)
                    if d >= now_d :
                        pos.append((now_d, i, j))
        pos.sort(key = (lambda x : (x[0], x[2])))

        if pos :
            attack_list.append(pos[0])

    for a in attack_list :
        _, i, j = a
        if temp[i][j] == 1 :
            temp[i][j] = 0
            cnt += 1
    return cnt

def move() :
    for i in range(-1, -n, -1) :
        temp[i] = temp[i-1]

    temp[0] = [0 for _ in range(m)]

def is_empty() :
    for i in range(n) :
        for j in range(m) :
            if temp[i][j] == 1 :
                return False
    return True

n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
items = [i for i in range(m)]
result = 0

for a in combinations(items, 3) :
    temp = copy.deepcopy(graph)
    count = 0
    while not is_empty() :
        count += attack(a)
        move()
    result = max(result, count)
print(result)






