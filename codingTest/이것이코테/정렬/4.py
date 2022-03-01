# 4. 두 배열의 원소 교체
# : A, B 두 배열은 N 개의 원소로 구성되어 있고, 모두 자연수
# : 최대 K 번 바꿔치기 가능하다
# : 바꿔치기는 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것
# : 배열 A의 모든 원소의 합이 최대가 되도록 하기

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k) :
    if a[i] < b[i] : 
        a[i], b[i] = b[i], a[i]
    else :
        continue

sum = 0
for i in a :
    sum += i
print(sum)