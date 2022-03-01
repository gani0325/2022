# 떡볶이 떡 만들기
# : 높이가 H보다 긴 떡은 잘리고, 낮은 떡은 잘리지 않음
# : 요청한 총 길이가 M일 때, 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하기
# : 떡의 개수 N, 떡의 길이 M

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end) :
    total = 0
    mid = (start + end) // 2
    for x in array :
        if x > mid :
            total += x - mid
    # 왼쪽
    if total < m :
        end = mid - 1
    # 오른쪽
    else :
        result = mid
        start = mid + 1
print(result)