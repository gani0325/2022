# 퇴사

#  N+1일째 되는 날 퇴사를 하기 위해서,
#  남은 N일 동안 최대한 많은 상담을 하려고 한다.

# 백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고,
# 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.

# 각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와
# 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

# 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램

n = int(input())
t = []
p = []
dp = ( [0] * (n+1) )
result = 0

for i in range(n) :
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1) :
    time = t[i] + i

    if time <= n :
        dp[i] = max(p[i] + dp[time], result)
        result = dp[i]
    else :
        dp[i] = result

print(result)
