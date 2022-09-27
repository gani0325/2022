# # 1. 10진수 -> 2진수 변환
# num = int(input())

# result = ""

# while num > 0 :
#     result = str(num % 2) + result
#     num //= 2

# print(result)

# # result
# # 10
# # 1010


# 2. 10진수 n 기수 변환
def convert(n, b) :
    result = ""
    while n > 0 :
        result = str(n%base) + result
        n //= b
    return result

num, base = map(int, input().split())
print(convert(num, base))

# result
# 18 3
# 200