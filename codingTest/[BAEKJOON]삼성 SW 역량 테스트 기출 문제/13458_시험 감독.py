# 시험 감독

# 총 N개의 시험장이 있고, 각각의 시험장마다 응시자들이 있다.
# i번 시험장에 있는 응시자의 수는 Ai명이다.

# 감독관은 총감독관과 부감독관으로 두 종류가 있다.
    # 총감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명이고,
    # 부감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명이다.

# 각각의 시험장에 총감독관은 오직 1명만 있어야 하고,
# 부감독관은 여러 명 있어도 된다.

# 각 시험장마다 응시생들을 모두 감시해야 한다.
# 이때, 필요한 감독관 수의 최솟값을 구하는 프로그램

n = int(input())
num = list(map(int, input().split()))
b, c = map(int, input().split())

b_num = 0
c_num = 0

for i in range(n) :
    num[i] = num[i] - b
    b_num += 1

for i in range(n) :
    if num[i] <= 0 :
        continue
    if num[i] % c == 0 :
        c_num += (num[i] // c)
    else  :
        c_num += (num[i] // c + 1)

print(c_num + b_num)