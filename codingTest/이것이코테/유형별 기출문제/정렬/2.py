# 1. 위에서 아래로
# : 주어진 수열을 내림차순으로 정렬

a = int(input())
list = []

for i in range(a) :
    b = int(input())
    list.append(b)

list.sort(reverse = True)

for i in list :
    print(i, end = " ")