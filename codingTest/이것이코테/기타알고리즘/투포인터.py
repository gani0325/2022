# 투 포인터
# : 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리
# - 시작점과 끝점이 첫 번째 원소의 인덱스 0 을 가리키도록 한다
# - 현재 부분합이 M과 같다면 카운트 한다
# - 현재 부분합이 M보다 작으면 end를 1 증가한다
# - 현재 부분합이 M보다 크거나 같으면 start을 1 증가한다
# - 모든 경우를 확인할 때까지 2~4 반복

n = int(input()) # 데이터 개수
m = int(input()) # 찾고자 하는 부분합
data = list(map(int, input().split()))

count = 0
interval_sum = 0
end = 0

# start 증가
for start in range(n) :
    # end를 가능한 만큼 이동
    while interval_sum < m and end < n :
        interval_sum += data[end]
        end += 1
    # 부분합이 m 일 때
    if interval_sum == m :
        count+= 1
    interval_sum -= data[start]

print(count)