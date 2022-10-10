# 2048 (easy)

# 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것
# 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다. 
# 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.
# (실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만, 이 문제에서 블록이 추가되는 경우는 없다)

# 똑같은 수가 세 개가 있는 경우에는 이동하려고 하는 쪽의 칸이 먼저 합쳐진다. 
# 이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다. 
# 보드의 크기와 보드판의 블록 상태가 주어졌을 때, 
# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성

# 첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다. 
# 0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다. 
# 블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다.
# 블록은 적어도 하나 주어진다.

# 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력

from copy import deepcopy
N = int(input())

graph = []
for i in range(N) :
    graph.append(list(map(int, input().split())))
result = 0

def left(graph) :
    for i in range(N) :
        # 열 가장 왼쪽
        p = 0
        x = 0
        for j in range(N) :
            # 빈칸
            if graph[i][j] == 0 :
                continue
            # 더할게 없다면
            if x == 0 :
                x = graph[i][j]
            # 더할게 있는데, 숫자가 같은가?
            else :
                if x == graph[i][j] :
                    graph[i][p] = x * 2
                    x = 0
                    p += 1
                else :
                    graph[i][p] = x
                    x = graph[i][j]
                    p += 1
            # 비워주기
            graph[i][j] = 0

        # 좌측에서 우측 끝까지 도달!
        if x != 0 :
            graph[i][p] = x

    return graph

def right(graph) : 
    for i in range(N) :
        # 가장 우측 열
        p = N - 1
        x = 0
        for j in range(N - 1, -1 , -1) :
            # 빈칸
            if graph[i][j] == 0 :
                continue
            # 더할게 없다면
            if x == 0 :
                x = graph[i][j]
            # 더할게 있는데, 숫자가 같은가?
            else :
                if x == graph[i][j] :
                    graph[i][p] = x * 2
                    x = 0
                    p -= 1
                else :
                    graph[i][p] = x
                    x = graph[i][j]
                    p -= 1
            # 비워주기
            graph[i][j] = 0

        # 우측에서 좌측 끝까지 도달!
        if x != 0 :
            graph[i][p] = x

    return graph

def up(graph) : 
    for i in range(N) :
        # 가장 위 행
        p = 0
        x = 0
        for j in range(N) :
            # 빈칸
            if graph[j][i] == 0 :
                continue
            # 더할게 없다면
            if x == 0 :
                x = graph[j][i]
            # 더할게 있는데, 숫자가 같은가?
            else :
                if x == graph[j][i] :
                    graph[p][i] = x * 2
                    x = 0
                    p += 1
                else :
                    graph[p][i] = x
                    x = graph[j][i]
                    p += 1
            # 비워주기
            graph[j][i] = 0

        # 위측에서 아래측 끝까지 도달!
        if x != 0 :
            graph[p][i] = x

    return graph

def down(graph) : 
    for i in range(N) :
        # 가장 아래 행
        p = N - 1
        x = 0
        for j in range(N - 1, -1 , -1) :
            # 빈칸
            if graph[j][i] == 0 :
                continue
            # 더할게 없다면
            if x == 0 :
                x = graph[j][i]
            # 더할게 있는데, 숫자가 같은가?
            else :
                if x == graph[j][i] :
                    graph[p][i] = x * 2
                    x = 0
                    p -= 1
                else :
                    graph[p][i] = x
                    x = graph[j][i]
                    p -= 1
            # 비워주기
            graph[j][i] = 0

        # 아래측에서 위측 끝까지 도달!
        if x != 0 :
            graph[p][i] = x

    return graph

def solution(graph, cnt) :
    global result

    if cnt == 5 :
        for i in range(N) :
            for j in range(N) :
                result = max(result, graph[i][j])
        return
    
    solution(left(deepcopy(graph)), cnt + 1)
    solution(right(deepcopy(graph)), cnt + 1)
    solution(up(deepcopy(graph)), cnt + 1)
    solution(down(deepcopy(graph)), cnt + 1)

solution(graph, 0)
print(result)

# input
# 3
# 2 2 2
# 4 4 4
# 8 8 8 

# output
# 16