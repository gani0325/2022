# 2. 시각
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수
# 경우의 수 86,400 가지

a = int(input())
cnt = 0

for i in range(a+1) :
    for j in range(60) :
        for k in range(60) :
            if '3' in str(i) + str(j) + str(k) :
                cnt += 1
print(cnt)

