# 부품 찾기
# : 부품 N개가 있는데, 손님이 요처한 부품 번호의 순서대로 확인해 부품이 있으면 yes, 없으면 no 출력

# by. 이진탐색
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
# 내 가게
n = int(input())
array = list(map(int, input().split()))
array.sort()
# 손님
m = int(input())
x = list(map(int, input().split()))

for i in x :
    result = binary_search(array, i, 0, n-1)
    if result != None  
        print("yes", end = " ")
    else :
        print("no", end = " ")




# by. 계수 정렬

# 내 가게
n = int(input())
array = [0] * 1000000

for i in input().split() :
    array[int(i)] = 1
  
# 손님
m = int(input())
x = list(map(int, input().split()))

for i in x :
    # 해당 부품 존재 확인
    if array[i] = None  :
        print("yes", end = " ")
    else :
        print("no", end = " ")


      
# by. set 함수

# 내 가게
n = int(input())
array = set(map(int, input().split()))
  
# 손님
m = int(input())
x = list(map(int, input().split()))

for i in x :
    # 해당 부품 존재 확인    
    if i in array :
        print("yes", end = " ")
    else :
        print("no", end = " ")