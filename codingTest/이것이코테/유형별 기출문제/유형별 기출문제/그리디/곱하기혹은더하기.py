# 곱하기 혹은 더하기
# : 0~9 로 이루어진 문자열 s가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 x, + 넣어 가장 큰 수를 구하라

num = input()
result = int(num[0])

for i in range(1, len(num)) :
    number = int(num[i])
  
    if 1 >= number or 1 >= result :
        result += number
    else :
        result *= number
print(result)