# 병사배치하기
# : N명의 병사가 무작위로 나열
# : 각 병사는 특정한 값의 전투력 보유, 병사 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치
# : 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야함
# : 남아있는 병사의 수가 최대

n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n

# 부분 수열 NIS 수행
for i in range(1, n) :
    for j in range(0, i) :
        if array[j] < array[i] :
            dp[i] = max(dp[i], dp[j] + 1)

print(n- max(dp))