# 개미 전사
# : 식량창고 N개가 주어졌을 때 얻을 수 있는 식량의 최댓값
# : 최소한 한 칸 이상 떨어진 식량창고 약탈해야됨

n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n) :
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])