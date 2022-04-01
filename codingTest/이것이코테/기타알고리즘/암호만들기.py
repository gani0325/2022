# 암호 만들기
# : 암호는 서로 다른 L개의 알파벳 소문자로 구성, 최소 한개의 모음과 최소 두개의 자음으로 구성
# : 알파벳이 암호세어 증가하는 순서로 배열
# : 조교들이 암호로 사용했을 법한 문자의 종류는 C가지
# : C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하라

from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split(' '))

# 사전식으로 출력
array = input().split(' ')
array.sort()

# 길이가 l인 모든 암호 조합
for password in combinations(array, l) :
    count = 0
    for i in password :
        if i in vowels :
            count += 1

    if count >=1 and count <= l-2 :
        print("".join(password))
