# 2. 큰수의 법칙
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 초과하여 더해질 수 없는 것이 특징
# 배열의 크기N, 숫자가 더해지는 횟수 M, K가 주어질 때 큰 수를 찾아라

n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
first = num[n-1]
second = num[n-2]
result = 0

while True :
    for j in range(k) :
        if m == 0:
            break
        result += first
        m -= 1 
    if m == 0 :
        break
    result += second
    m -= 1
print(result)


# 2.1
n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
first = num[n-1]
second = num[n-2]
result = 0

# 가장 큰 수 더해지는 횟수 
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m - count) * second
print(result)