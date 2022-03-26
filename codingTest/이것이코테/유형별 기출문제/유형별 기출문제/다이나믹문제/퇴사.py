# 퇴사
# : 오늘부터 N+1일 째 되는 날 퇴사를 위해, N일 동안 많은 상담 하려고 한다
# : 상담을 완료하는데 걸리는 시간 T와 받을 수 있는 금액 P
# : 상담 필요 기간은 1일 보다 클 수 있기 때문에, 모든 상담 X
# : 상담을 적절히 했을 때, 백준이가 얻을 수 이는 최대 수익은?

n = int(input())
t = []     # 상담 완료 시간
p = []     # 받는 금액
dp = [0] * (n + 1)
max_value = 0

for _ in range(n) :
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1) :
    time = t[i] + i
    # 상담이 기간 안에 끝남
    if time <= n :
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else :
        dp[i] = max_value

print(max_value)