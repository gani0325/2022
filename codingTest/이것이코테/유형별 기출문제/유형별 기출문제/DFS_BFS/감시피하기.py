# 감시 피하기
# : N X N 크기의 복도
# : 특정한 위치에 선생님, 학생, 장애물
# : 선생님은 상, 하, 좌, 우로 감시 진행
# : 선생님은 T, 학생은 S, 장애물은 O
# : 위치값은 (행, 열)
# : 학생들은 복도의 빈칸 중에서 장애물을 설치할 위치를 골라, 정확히 3개의 장애물을 설치해야 함

from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n) :
    board.append(list(input().split()))
    for j in range(n) :
        if board[i][j] == 'T' :
            teachers.append((i, j))
        if board[i][j] == 'X' :
            spaces.append((i, j))

def watch(x, y, direction) :
    if direction == 0 :
        while y >= 0 :
            if board[x][y] == 'S' :
                return True
            if board[x][y] =='O' :
                return False
            y -= 1
    if direction == 1 :
        while y < n :
            if board[x][y] == 'S' :
                return True
            if board[x][y] == 'O' :
                return False
            y += 1
    if direction == 2 :
        while x >= 0 :
            if board[x][y] == 'S' :
                return True
            if board[x][y] == 'O' :
                return False
            x -= 1
    if direction == 3:
        while x < n :
            if board[x][y] == 'S' :
                return True
            if board[x][y] == 'O' :
                return False
            x += 1
    return False

def process() :
    for x, y in teachers :
        for i in range(4) :
            if watch(x, y, i) :
                return True
    return False

find = False

for data in combinations(spaces, 3) :
    for x, y in data :
        board[x][y] = 'O'
    if not process() :
        find = True
        break
    for x, y in data :
        board[x][y] = 'X'

if find :
    print("YES")
else :
    print("NO")
