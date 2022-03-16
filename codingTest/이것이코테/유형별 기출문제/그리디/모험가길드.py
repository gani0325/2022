# 모험가 길드
# : N명의 모험가가 있을 때, 여행을 떠날 수 있는 그룹 수의 최대값
# : 공포도가 X인 모험가는 반드시 X명 이상으로 구성되어야 함


n = int(input())
export = list(map(int, input().split()))
count = 0
result = 0

export.sort()

for i in export :  
    count += 1
    if export[i] <= count :
        result += 1
        count = 0
print(result)