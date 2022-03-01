# 정렬
# : 데이터를 특정한 기준에 따라서 순서대로 나열하는 것

# 1. 선택 정렬
# : 가장 작은 데이터를 선택해, 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복
# : O(N^2)

array = [3, 4, 7, 1, 2 ,5 ,8 ,9,6]

for i in range(len(array)) :
    min_index = i
    for j in range(i + 1, len(array)) :
        if array[min_index] > array[j] :
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
print(array)    


# 2. 삽입 정렬
# : 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입하자
# : 특정한 데이터를 적절한 위치에 삽입한다
# : 두 번째 데이터부터 시작
# : O(N^2)

array = [3, 4, 7, 1, 2, 5, 8, 9, 6]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            continue

print(array)


# 3. 퀵 정렬
# : 기준 데이터를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸자
# : 교환하기 위한 기준을 피벗이라 한다
# 호어분할
# - 리스트에서 첫 번째 데이터를 피벗으로 정한다
# - 왼쪽에서 피벗보다 큰 데이터 선택, 오른쪽에서 피벗보다 작은 데이터 선택 ( 두 데이터 바꿈 )
# - 서로 엇갈린 경우, 작은 데이터와 피벗 위치 바꾼다
# - 왼쪽 리스트는 피벗보다 작고, 오른쪽 리스트는 피벗보다 크다 (분할, 파티션)
# - 왼쪽 파티션끼리, 오른쪽 파티션 기리 다시 퀵 정렬을 한다
# - 퀵 정렬의 끝나는 조건은 현재 리스트의 데이터 개수가 1개일 경우
# : O(NlogN)


array = [3, 4,0,  7, 1, 2, 5, 8, 9, 6]

def quick_sort(array, start, end) :
    if start >= end :
        return
    
    pivot = start
    left = start + 1
    right = end
    
    while left <= right :
        # 피벗보다 큰 데이터
        while left <= end and array[left] <= array[pivot] :
            left += 1
        # 피벗보다 작은 데이터
        while right > start and array[right] >= array[pivot] :
            right -= 1
        # 엇갈리면
        if left > right :
            array[right], array[pivot] = array[pivot], array[right]
        else :
            array[right], array[left] = array[left], array[right] 
        
    # 분할 이후, 왼 오른쪽 정렬 ㄱ
    quick_sort(array, start, right - 1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# 3.1 파이썬 + 퀵 정렬
array = [6, 8, 1, 4, 3, 5, 2, 9, 7, 0]

def quick_sort(array) :
    if len(array) <= 1 :
        return array
    
    pivot = array[0]
    tail = array[1:] # 피벗 제외 리스트

    left_side = [x for x in tail if x < pivot]
    right_side = [x for x in tail if x > pivot]

    # 분할이후
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array))


# 4. 계수 정렬
# : 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
# : O(N + K)
# : 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용
# : 모든 범위를 담을 수 있는 크기의 리스트를 선언
# : O(N + K) ( 데이터 개수 N, 데이터 중 최대값 크기 K)

array = [1, 6, 8, 9, 2,2, 6, 4, 2,4, 3, 7]
cnt = [0] * (len(array) + 1)

for i in range(len(array)) :
    cnt[array[i]] += 1 # 각 데이터 해당하는 인덱스 값 증가

for i in range(len(cnt)) :
    for j in range(cnt[i]) :
        print(i, end= " ")


# 5. 파이썬 정렬 라이브러리
# - O(NlogN)

# - sorted
array = [ 8, 3, 5, 6, 4, 7, 2, 1, 9]
print(sorted(array))

# - sort
array = [ 8, 3, 5, 6, 4, 7, 2, 1, 9]
array.sort()
print(array)

# - key
array = [("바나나", 2), ("사과", 1), ("딸기", 5)]
def setting(data) :
    return data[1]
result = sorted(array, key = setting)
print(result)



# - 정렬 라이브러리로 풀기
# - 정렬 알고리즘 원리로 풀기
# - 더 빠른 정렬이 필요하면? 