# 4. 1이 될 때까지
# 어떠한 수 N이 1이 될 때가지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
# 두번 째 연산은 N이 K로 나누어질 때만 선택 가능
# - N에서 1 뺀다
# - N을 K로 나눈다
# N이 1이 될 때까지 1번, 2번의 과정을 수행해야하는 최소 횟수 구하기

n, k = map(int, input().split())
result = 0

while n >= k :
    while n % k != 0 :
        n -= 1
        result +=1
    n /= k
    result += 1

while n > 1 :
    n -= 1
    result += 1
print(result)    


# 4.1
n, k = map(int, input().split())
result = 0

while True :
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k :
        break
    
    result += 1
    n /= k

result += (n-1)
print(result)    