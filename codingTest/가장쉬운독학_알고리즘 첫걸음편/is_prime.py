# # 소수 판별하기
# # 소수란 1과 자기 자신만을 약수로 갖는 수

## 1. 소수 찾기
# import math

# num = int(input())

# def is_prime(n) :
#     if n <= 1 :
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1) :
#         if n % i == 0 :
#             return False
#     return True

# print(is_prime(num))

# # # result
# # 13
# # True

# # 10
# # False


# # 2. 100000 까지 소수 찾기 몇초 걸릴까?
# import math, time

# def is_prime(n) :
#     if n <= 1 :
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1) :
#         if n % i == 0 :
#             return False
#     return True

# def time_is_prime(m) :
#     for i in range(m) :
#         if is_prime(i) :
#             print(i, end = " ")

# start = time.time()
# time_is_prime(100000)
# end = time.time()

# print("\n")
# print(end-start)

# # result
# # 0.31109094619750977


# 3. 에라토스테네스의 체
# : 지정된 범위 내에서 2로 나누어떨어지는 수, 3 ... 등등 나누어 떨어지는 수를 차례로 제외하면 마지막엔 소수만 남는다

import math, time
def get_prime(n) :
    if n <= 1 :
        return []
    prime = [2]
    limit = int(math.sqrt(n))

    # 홀수 리스트
    data = [i + 1 for i in range(2, n, 1)]

    while limit >= data[0] :
        prime.append(data[0])
        # 나누어 떨어지지 않는 수만 append
        data = [j for j in data if j % data[0] != 0]
    return prime + data

start = time.time()
get_prime(100000)
end = time.time()

print("\n")
print(end-start)

# result
# 0.06504034996032715