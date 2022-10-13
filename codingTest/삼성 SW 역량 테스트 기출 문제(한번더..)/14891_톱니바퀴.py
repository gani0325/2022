# 톱니바퀴

# 총 8개의 톱니를 가지고 있는 톱니바퀴 4개
#     톱니는 N극 또는 S극 중 하나를 나타내고 있다.
#     가장 왼쪽 톱니바퀴가 1번, 그 오른쪽은 2번, 
#     그 오른쪽은 3번, 가장 오른쪽 톱니바퀴는 4번

# 톱니바퀴를 총 K번 회전시키려고 한다.
# 톱니바퀴의 회전은 한 칸을 기준으로 한다. 
# 회전은 시계 방향과 반시계 방향

# 톱니바퀴를 회전시키려면, 회전시킬 톱니바퀴와 회전시킬 방향을 결정
# 회전할 때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고, 회전시키지 않을 수도 있음
# 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면,
#  B는 A가 회전한 방향과 반대방향으로 회전하게 된다. 

# 톱니바퀴의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때, 
# 최종 톱니바퀴의 상태를 구하는 프로그램을 작성

# 첫째 줄에 1번 톱니바퀴의 상태, 둘째 줄에 2번 톱니바퀴의 상태, 셋째 줄에 3번 톱니바퀴의 상태, 넷째 줄에 4번 톱니바퀴의 상태
#     상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다.
#     N극은 0, S극은 1
# 다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)가 주어진다.
# 다음 K개 줄에는 회전시킨 방법이 순서대로 주어진다.
#     두 개의 정수 : 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향
#     방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향

# 총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력
#     1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
#     2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
#     3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
#     4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점


# 1) DFS

import  collections

graph = []
# for i in range(4) :
#     graph.append(list(map(int, input())))
for _ in range(4):
    graph.append(collections.deque(list(input())))

# K개 줄에는 회전시킨 방법
K = int(input())

# 톱니 맞물리는 상태 저장
info = [list(map(int, input().split())) for _ in range(K)] 

# 왼쪽
def left(n, d) :
    if n < 0 :
        return
    if graph[n][2] != graph[n + 1][6] :    # 극 비교
        left(n-1, -d)       # 왼쪽 조사
        graph[n].rotate(d)

# 오른쪽
def right(n, d) :
    if n > 3 :
        return
    if graph[n][6] != graph[n - 1][2] :    # 극 비교
        right(n+1, -d)       # 오른쪽 조사
        graph[n].rotate(d)

for i in range(K) :
    num = info[i][0] - 1        # 톱니바퀴
    direction = info[i][1]      # 시계, 반시계
    left(num - 1, -direction)
    right(num + 1, -direction)
    graph[num].rotate(direction)

result = 0

if graph[0][0] == '1':
    result += 1
if graph[1][0] == '1':
    result += 2
if graph[2][0] == '1':
    result += 4
if graph[3][0] == '1':
    result += 8

print(result)