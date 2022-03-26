# 정렬된 배열에서 특정 수의 개수 구하기
# : N개의 원소를 포함하고 있는 수열이 오름차순 정열
# : 수열에서 x가 등장하는 횟수 계산
# : O(logN)
# : 이진탐색이란 탐색 범위를 반으로 줄여나가면서 데이터를 빠르게 탐색

# 1. 일반 선형 탐색
num = list(map(int, input().split()))
num_list = list(map(int, input().split()))
count = 0


for i in range(num[0]) :
    if num_list[i] == num[1] :
        count += 1
    else :
        count = -1

print(count)



# 2. 이진 탐색

def count_by_value(array, x) :
    n = len(array)
    # 처음 등장
    a = first(array, x, 0, n-1)
    if a == None :
        return 0
    # 마지막 등장
    b = last(array, x, 0, n-1)
    return b- a +1

def first(array, target, start, end) :
    if start  > end :
        return None
    mid = (start + end) // 2
    # 가장 왼쪽 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target :
        return mid

    elif array[mid] >= target :
        return first(array, target, start, mid - 1)

    else : 
        return first(array, target, mid+1, end)

# 마지막 위치 찾기
def last(array, target, start, end) :
    if start > end :
        return None
    mid = (start + end) // 2
    # 가장 오른쪽 인덱스 반환
    if (mid == n-1 or target < array[mid+1]) and array[mid] == target :
        return mid
    # 중간보다 작으면 왼쪽
    elif array[mid] > target :
        return last(array, target, start, mid -1)
    # 중간보다 크거나 같으면 오른쪽
    else :
        return last(array, target, mid +1, end)

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)

if count == 0 :
    print(-1)

else : 
    print(count)