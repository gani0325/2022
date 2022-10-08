# 스타트링크

# 오늘은 강호의 면접날이다. 
# 늦잠을 잔 강호는 스타트링크가 있는 건물에 늦게 도착하고 말았다.

# 스타트링크는 총 F층으로 이루어진 고층 건물에 사무실이 있고, 
# 스타트링크가 있는 곳의 위치는 G층이다.
# 강호가 지금 있는 곳은 S층이고, 이제 엘리베이터를 타고 G층으로 이동하려고 한다.

# 보통 엘리베이터에는 어떤 층으로 이동할 수 있는 버튼이 있지만, 
# 강호가 탄 엘리베이터는 버튼이 2개밖에 없다. 

# U버튼은 위로 U층을 가는 버튼, D버튼은 아래로 D층을 가는 버튼이다.
#  (만약, U층 위, 또는 D층 아래에 해당하는 층이 없을 때는, 엘리베이터는 움직이지 않는다)

# 강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하는 프로그램을 작성
# 엘리베이터를 이용해서 G층에 갈 수 없다면, "use the stairs"를 출력한다.

# 첫째 줄에 F, S, G, U, D가 주어진다. 
# (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000) 건물은 1층부터 시작하고, 
# 가장 높은 층은 F층이다.

# 첫째 줄에 강호가 S층에서 G층으로 가기 위해 눌러야 하는 버튼의 수의 최솟값을 출력
# 만약, 엘리베이터로 이동할 수 없을 때는 "use the stairs"를 출력

# 1) BFS
from collections import deque

# 건물높이, 강호위치, 사무실위치, 올라가야되는 층, 내려가야되는 층
F, S, G, U, D = map(int, input().split())

def bfs(s, g) :
    visited = [-1] * (F + 1)

    # 현재 강호 위치
    q = deque([s])
    visited[s] = 0

    while q :
        x = q.popleft()

        # 사무실에 도착
        if x == g :
            return visited[x]
        
        UP = x + U
        DOWN = x - D

        if (UP <= F) and (visited[UP] == -1) :
            q.append(UP)
            visited[UP] = visited[x] + 1

        if (DOWN > 0) and (visited[DOWN] == -1) :
            q.append(DOWN)
            visited[DOWN] = visited[x] + 1

    return "use the stairs"

print(bfs(S, G))

# input
# 10 1 10 2 1
# output
# 6

# input
# 100 2 1 1 0
# output
# use the staris