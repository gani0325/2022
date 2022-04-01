# 에라토스테네스의 체
# : 여러개의 수가 소수인지 아닌지를 판별
# : N보다 작거나 같은 모든 소수를 찾을 때 사용
# - 2부터 N까지의 모든 자연수 나열
# - 남은 수 중 아직 처리하지 않은 가장 작은 수 i 찾기
# - 남은 수 중 i의 배수를 모두 제거 (i는 제거 X)
# - 더 이상 반복할 수 없을 때까지 2,3 반복

import math

n = 1000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1) :
    if array[i] == True :    # 소수이면
        j = 2
        while i * j <= n :
            array[i * j] = False
            j += 1

for i in range(2, n+1) :
    if array[i] :
        print(i, end= " ")