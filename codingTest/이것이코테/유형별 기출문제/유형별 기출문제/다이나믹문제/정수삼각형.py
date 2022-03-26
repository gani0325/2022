# 정수 삼각형
# : 맨 위층에서 아래에 있는 수 하나를 선택하여 아래로 내려올 대, 선택 된 수의 합이 최대가 되는 경로 구하기
# : 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택 가능

n = int(input())
dp = []

for _ in range(n) :
    dp.append(list(map(int, input().split())))

for i in range(1, n) :
    for j in range(i+1) :
        # 왼쪽 위
        if j == 0:
            up_left = 0
        else :
            up_left = dp[i-1][j-1]
        # 바로 위
        if j == i:
            up = 0
        else :
            up = dp[i-1][j]
        # 최대 합
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n-1]))