# 고정점 찾기
# : 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
# : 하나의 수열이 N개의 서로 다른 원소를 포함하고 있고, 모든 원소가 오름차순으로 정렬
# : 이 수열에 고정점이 있다면, 고정점 출력! 없으면 -1
# : O(logN)

def binary_search (array, start, end) :
    if start > end :
        return None
    mid = (start + end) // 2
    # 고정점 찾으면
    if array[mid] == mid :
        return mid
    # 중간점이 더 작을 경우 왼쪽
    elif array[mid] > mid : 
        return binary_search(array, start, mid - 1)
    else :
        return binary_search(array, mid+1, end)

n = int(input())
array = list(map(int, input().split()))

index = binary_search(array, 0, n-1)

if array == None :
    print(-1)
else :
    print(index)