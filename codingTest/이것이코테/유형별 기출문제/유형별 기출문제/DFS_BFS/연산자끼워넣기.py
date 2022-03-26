# 연산자 끼워 넣기
# : N개의 수로 이루어진 수열 
# : 수와 수 사이에 끼워 넣을 수 있는 N-1 개의 연산자
# : 주어진 수의 순서 바꾸면 안된다
# : 연산자 우선순위 무시하고 앞에서 진행
# : 나눗셈은 몫
# : N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것은?
# : DFS

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now) :
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else :
        if add > 0 :
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0 :
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0 :
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0 :
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)