# 자물쇠와 열쇠
# : 잠겨있는 자물쇠는 격자 한 칸의 크기가 1X1인 NXN 크기의 정사각 격자 형태
# : 특이한 모양의 열쇠는 MXM 크기인 정사각 격자 형태
# : 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분은 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열림
# : 열쇠를 나타내는 2차원 배열 key, 자물쇠를 나타내는 2차원 배열 lock이 매개변수,
# : 열쇠로 자물쇠 열 수 있으면 true, 열 수 없으면 false return 하는 solution 함수
# : key, lock 원소는 0, 1(0은 홈, 1은 돌기)

def rotate_a_matrix_by_90_degree(a) :
    n = len(a)  # 행
    m = len(a[0])  # 열

    result = [[0] * n for _ in range(m)]
    for i in range(n) :
        for j in range(m) :
            result[j][n - i - 1] = a[i][j]
    return result

def check(new_lock) :
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2) :
        for j in range(lock_length, lock_length * 2) :
        if new_lock[i][j] != 1 :
            return False
    return True

def solution(key, lock) :
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n * 3) for _ in range(n*3)]
    for i in range(n) :
        for j in range(n) :
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4) :
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n*2) :
            for y in range(n*2) :
                for i in range(m)  :
                    for j in ramge(m) :
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock)
 == True :
                    return True
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j] -= key[i][j]
    return False