# 피보나치 수열
# : 첫째 및 둘째 항이 1이고, 그 뒤 모든 항은 바로 앞의 두 항을 합한 수열

"""
# 1. 피보나치 수열 구하기
def fibonacci (n) :
    if (n == 1) or (n == 2) :
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# result
# 55
"""


"""
# 2. 메모이제이션으로 처리속도 향상
# : memo는 처리 결과를 사전에 등록해놓고 그 값을 반환한다

memo = {1 :1, 2 : 1}

def fibonacci(n) :
    if n in memo :
        return memo[n]

    memo[n] = fibonacci(n-1) + fibonacci(n-2)

    return memo[n]

print(fibonacci(10))

# result
# 55
"""


# 3. 반복문으로 피보나치 수열
def fibonacci(n) :
    fib = [1, 1]
    for i in range(2, n) :
        fib.append(fib[i-1] + fib[i-2])
    return fib[n-1]

print(fibonacci(7))

# result
# 7