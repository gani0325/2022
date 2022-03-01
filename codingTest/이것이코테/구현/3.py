# 3. 왕실의 나이트
# 체스판 8x8
# 나이트는 이동 할 때 L 형태로 이동
# - 수평으로 두 칸 이동 후 수직으로 한 칸 이동
# - 수직으로 두 칸 이동 후 수평으로 한 칸 이동
# 나이트의 위치 주어졌을 때, 나이트가 이동할 수 있는 경우의 수
# 행 위치 1 ~ 8
# 열 위치 a ~ h
# 나이트 위치 좌표는 두 문자로 구성된 문자열 ex) a3

data = input()
row = int(data[1])
cols = int(ord(data[0])) - int(ord("a")) + 1
# ord : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환

step = [(-2,1), (-2,-1), (2, 1), (2, -1), (-1, -2), (1, -2), (-1, 2),(1, 2)]

result = 0
for i in step :
    next_row = row + i[0]
    next_cols = cols + i[1]

    if next_row >= 1 and next_cols >=1 and next_row <= 8 and next_cols <= 8 :
        result += 1
print(result)