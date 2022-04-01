# 구간 합 계산
# : 연속적으로 나열된 n개의 수가 있을 때, 특정 구간의 모든 수를 합한 깂
# : 여러 개의 쿼리로 구성
# : 다수의 구간에 대해서 합을 각각 구하라
# : 접두사 합, 리스트의 맨 앞부터 특정 위치까지의 합을 구해 놓는 것

n = int(input())
data = list(map(int, input().split()))

# 접두사 합 배열
sum_value = 0
prefix_sum = [0]
for i in data :
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])