# 공유기 설치
# : 집이 N개의 수직 선 위에 있음
# : 각  집은 x1, x2, ...
# : 집에 C개의 공유기 설치하려 함
# : 한 집에 하나만 설치. 가장 인접한 두 공유기 사이의 거리를 가능한 크게
# : C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대화 하라

n, c = list(map(int, input().split()))

array = []
for _ in range(n) :
    array.append(int(input()))

array.sort()

start = array[1] - array[0]    # 집 좌표 중 작은 값
end = array[-1] - array[0]     # 집 좌표 중 큰 값
result = 0

while (start <= end) :
    mid = (start + end) // 2 # 거리
    value = array[0]
    count = 1

    for i in range(1, n) :
        if array[i] >= value + mid :
            value = array[i]
            count += 1
    if count > c :    # c개 이상 설치 할 수 있으면, 거리 증가
        start = mid + 1
        result = mid
    else :
        end = mid -1

print(result)