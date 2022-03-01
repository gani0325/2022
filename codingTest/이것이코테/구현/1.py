# 구현
# - 완전탐색 : 모든 경우의 수를 다 계산
# - 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행

# 1. 상하좌우
# N X N 정사각형 공간에 1X1 크기의 정사각형으로 나누어져 있음
# 가장 왼쪽 위 좌표는 (1,1) 가장 오른쪽 아래 좌표는 (N,N)
# 상하좌우 움직이며, 시작좌표는 (1,1)
# L : 왼쪽 한칸
# R : 오른쪽 한칸
# U : 위로 한칸
# D : 아래로 한칸
# 계획서가 주어졌을 때 여행자 A 가 최종 도착의 좌표를 출력(X, Y)


n = int(input())
data = input().split()
x, y = 1, 1

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
move = ["L", "R", "U", "D"]

for i in data :
    for j in range(len(move)) :
        if i == move[j] :
            nx = x + dx[j]
            ny = y + dy[j]

    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    x, y = nx, ny

print(x, y) 