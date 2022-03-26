# 금광
# : n x m 크기의 금광
# : m번에 걸쳐서 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동
# : 채굴자가 얻을 수 있는 금의 최대 크기 출력

# : 점화식이란, 인접한 항들 사이의 관계식
# : 한 번 해결된 부분 문제의 정답을 메모리에 기록, 한 번 계산한 답은 다시 계산하지 않음
# : 탑다운은 재귀 함수를 이용해 큰 문제하기위해 작은 문제 호출
# : 보텀업은 반복문을 이용하여 작은 문제 먼저 해결하고 모아서 큰 문제 해결

for tc in range(int(input())) :
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n) :
        dp.append(array[index:index + m])
        index += m
    for j in range(1, m) :
        for i in range(n) :
            if i == 0:
                left_up = 0
            else : 
                left_up = dp[i-1][j-1]
            if i == n - 1:
                left_down = 0
            else :
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n) :
        result = max(result, dp[i][m-1])
    print(result)