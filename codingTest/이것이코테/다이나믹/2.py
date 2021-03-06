# 1로 만들기
# - X가 5로 나누어떨이지면, 5로 나눈다
# - X가 3으로 나누어떨어지면, 3으로 나눈다
# - X가 2로 나누어떨어지면, 2로 나눈다
# - X에서 1 뺀다
# : X가 주어졌을 때, 연산 4개로 1을 만들려고 함. 연산 사용 최소의 횟수

x = int(input())
d = [0] * 30001

for i in range(2, x+1) :
    d[i] = d[i-1] + 1
    if i % 5 == 0 :
        d[i] = min(d[i], d[i//5] + 1)
    if i % 3 == 0 :
        d[i] = min(d[i], d[i//3] + 1)
    if i % 2 == 0 :
        d[i] = min(d[i], d[i//2] + 1)

print(d[x])