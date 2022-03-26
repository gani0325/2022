# 문자열 재정렬
# : 알파벳 대문자와 숫자(0~9)로 구성된 문자열이 입력으로 주어진다
# : 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤, 그 뒤에 모든 숫자를 더한 값을 이어서 출력


mixed = input()

mixed = sorted(mixed)
char_list = []
sum = 0

for i in mixed :
    if i.isalpha() :
        char_list.append(i)
    else :  
        sum += int(i)

char_list.append(sum)

for j in char_list :
    print(j, end = "")