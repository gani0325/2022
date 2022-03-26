# 구현문제
# - 완전 탐색 : 모든 경우의 수를 빠짐없이 다 계산
# - 시뮬레이션 : 문제에서 제시하는 논리나 동작 과정을 그대로 코드로 옮겨야 하는 유형

# 럭키스트레이트
# : 현재 캐릭터의 점수를 N이라고 할 때 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황
# : 현재 점수 N이 주어지면 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지 알려주기 (사용 O : LUCKY, X : READY)


num = input()

half = 0
left = 0
right = 0

half = len(num) // 2

for j in range(half) :
    left += int(num[j])
for k in range(half, len(num)) :
    right += int(num[k])

print(left)
print(right)

if left == right :
    print("LUCKY")
else :
    print("READY")
  