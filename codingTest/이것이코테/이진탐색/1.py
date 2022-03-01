# 1. 범위를 반씩 좁혀가는 순차 탐색
# : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
# : O(N)

def sequential_search(n, target, array) :
    # 각 원소 하나씩 확인
    for i in range(n) :
        # 현재 원소와 찾고자하는 원소와 같을 경우
        if array[i] == target :
              return i + 1
print("생성 원소 개수 입력 하고 찾을 문자열 입력")
input_data = input().split()

n = int(input_data[0])
target = input_data[1]

print("원소 개수 만큼 문자열 입력")
array = input().split()

print(sequential_search(n, target, array))




# 2. 이진탐색
# : 배열 내부의 데이터가 정렬되어야만 사용
# : 탐색하고자 하는 범위의 시작점, 끝점, 중간점
# : 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 찾기
# : 한 번 확인할 때마다 확인하는 원소의 개수 절반씩 줄어든다
# : 재귀함수 + 반복문
# : O(lonN)

# 2.1 재귀함수
def binary_search(array, target, start, end) :
    if start > end :
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target :
        return binary_search(array, target, start, mid - 1)
    else :
        return binary_search(array, target, mid + 1, end)
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None :
    print("원소 존재 x")
else :
    print(result + 1)



# 2.2 반복문
def binary_search(array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2
        if array[mid] == target :
            return mid
        elif array[mid] > target :
            end = mid - 1
        else :
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None :
    print("원소 존재 x")
else :
    print(result + 1)


# 빠르게 입력받기
import sys
data = sys.stdin.readline().rstrip()

print(data)