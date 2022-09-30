# 이진검색
# 리스트의 왼쪽 끝과 오른쪽 끝에서부터 찾는 위치를 절반으로 좁히면서 검색


data = [10, 15 , 22, 26, 38, 42, 56, 61]
def binary_search (data, value) :
    left = 0
    right = len(data) - 1

    while left <= right :
        mid = (left + right) // 2

        if data[mid] == value :
            return mid
        
        elif data[mid] < value :
            left = mid + 1
        
        else :
            right = mid - 1
    return False

print(binary_search(data, 61))

# result
# 7