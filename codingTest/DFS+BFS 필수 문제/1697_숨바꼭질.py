# 숨바꼭질

# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
# 수빈이는 걷거나 순간이동을 할 수 있다. 

# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.


# 1) BFS
from collections import deque

N, K = map(int, input().split())

# 움직일 수 있는 최대 자표
max_num = 100000
# 시간
visited = [0] * (max_num + 1)       

def bfs() :
    q = deque()

    # 수빈이 큐
    q.append(N)

    while q : 
        x = q.popleft()

        if x == K :     # 같다면
            print(visited[x])
            break
        
        for j in (x-1, x+1, x*2) :
            # 주어진 범위 내에 있고, 아직 방문하지 않음
            if 0 <= j <= max_num and not visited[j] :
                # 이동한 위치에 시간 표시
                visited[j] = visited[x] + 1
                q.append(j)

bfs()

# input
# 3 17

# output
# 4