# 볼링공 고르기
# : A, B가 서로 무게가 다른 볼링공 고른다
# : 총 N개의 볼링공이 있고 1번부터 순수대로 부여
# : 같은 무게의 공이 여러개 있을 수 있고, 서로 다른 공으로 간주
# : 볼링공 무게는 1~M 자연수 형태로 존재
# : N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공 고르는 경우의 수

n, m = map(int, input().split())
ball = list(map(int, input().split()))

array = [0] * n
result = 0

for i in ball :
    array[i] += 1

for i in range(1, m+1) :
    n -= array[i]
    result += array[i] * n

print(result)