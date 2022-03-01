# 그리디
# 현재 상황에서 지금 당장 좋은 것만 고르는 방법

# 1. 거스름돈
a = int(input())
coin = [500, 100, 50, 10]
cnt = 0

for i in coin :
    cnt += a // i
    a %= i
print(cnt)