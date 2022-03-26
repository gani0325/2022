# 1. 성적이 낮은 순서로 학생 출력
# : N명의 학생의 이름과 성정이 주어졌을 때, 성적이 낮은 순서대로 학생의 이름 출력

a = int(input())
list = []

for i in range(a) :
    input_data = input().split()
    list.append((input_data[0], int(input_data[1])))

list = sorted(list, key = lambda num : num[1])

for num in list :
    print(num[0], end = " ")