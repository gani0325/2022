# 3. 숫자 카드 게임
# 가장 높은 숫자가 쓰인 카드 한장 뽑기
# N X M
# 행을 고르고, 해당 행에서 가장 숫자가 낮은 카드 고르고
# 최종적으로 가장 높은 숫자의 카드 뽑기

n, m = map(int, input().split())
result = 0

for i in range(n) :
    num = list(map(int, input().split()))

    min_num = min(num)
    result = max(result, min_num)
print(result)

# 3.1
n, m = map(int, input().split())
result = 0

for i in range(n) :
    num = list(map(int, input().split()))

    min_num = 10001

    for i in num :
        min_num = min(min_num, i)
    result = max(result, min_num)

print(result)    
