# 2차원 리스트를 90도 회전하는 메서드

def rotate_a_matrix_by_90_degree(a) :
    row_length = len(a)
    column_length = len(a)

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length) :
        for c in range(column_length) :
            res[c][row_length -1 -r] = a[r][c]

    return res

# a = [ ~ ~~ ~] 리스트
print(rotate_a_matrix_by_90_degree(a))
        