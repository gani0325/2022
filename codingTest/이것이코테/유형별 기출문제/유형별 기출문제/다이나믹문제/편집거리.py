# 편집 거리
# : 두 개의 문자열 A, B가 주어졌을 때, 문자열 A를 편집하여 문자열 B로 만들자
# - 삽입 : 특정 위치에 하나 문자 삽입
# - 삭제 : 특정 위치에 하나 문자 삭제
# - 교체 : 특저 위치에 하나 문자 교체
# : A를 B로 만드는 최소 편집 거리 계산

# : 행과 열 문자가 같다면, 왼쪽 위 해당하는 수 그대로 대입
# : 행과 열 문자가 다르다면, 왼쪽(삽입), 위쪽(삭제), 왼쪽 위(교체) 에 해당하는 수 중 가장 작은 수에 1 더해 삽입

def edit_dist(str1, str2) :
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1) :
        dp[i][0] = i
    for j in range(1, m+1) :
        dp[0][j] = j

    for i in range(1, n+1) :
        for j in range(1, m+1) :
            # 같다면 왼쪽 위 해당 수 그대로 삽입
            if str1[i-1] == str2[j-1] :
                dp[i][j] = dp[i-1][j-1]
            # 다르다면, 삽입, 삭제, 교체 중 최소 비용 삽입
            else :
                dp[i][j] = 1 +min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    return dp[n][m]

str1 = input()
str2 = input()

print(edit_dist(str1, str2))