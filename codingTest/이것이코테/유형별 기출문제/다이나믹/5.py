# 효율적인 화폐 구성
# : N가지 종류의 화폐, 개수를 최소한으로 해서 가치의 합이 M원이 되도록 함
# : 화폐 몇개라도 사용 가능

n, m = map(int, input().split())
array = []

for i in range(n) :
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n) :
    for j in range(array[i], m+1) :
        if d[j - array[i]] != 10001 :
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001 :
    print(-1)
else :
    print(d[m])