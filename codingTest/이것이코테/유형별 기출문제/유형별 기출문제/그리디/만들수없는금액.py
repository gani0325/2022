# 만들 수 없는 금액
# : N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하라

n = int(input())
coins = list(map(int, input().split()))

coins.sort()
target = 1

for i in coins :
    if i > target :
        break
    target += i
print(target)