# 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

# 스택
# : 박스 쌓기, 선입후출 구조 or 후입선출
stack = []
stack.append(5)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(3)
stack.append(6)
print(stack)
print(stack[::-1])

# 큐
# : 대기 줄
# 선입선출
from collections import deque

queue = deque()
queue.append(4)
queue.append(6)
queue.popleft()
queue.append(8)
queue.append(7)
queue.append(3)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# 재귀 함수 (스택 사용)
# : 자기 자신을 다시 호출하는 함수
def recursive_func ():
    print("재귀 함수 호출")
    recursive_func()
recursive_func()

def recursive_function(i) :
    # 100 출력 후 종료
    if i == 100 :
        return
    print(i, "번 째 재귀 함수에서 ", i+1, "번 재 재귀 함수 호출")
    recursive_function(i+1)
    print(i, "번째 재귀 함수 종료")
recursive_function(1)


# 팩토리얼
# - 반복적
def factorial_iterative(n) :
    result = 1
    for i in range(1, n+1) :
        result *= i
    return result

# - 재귀적
def factorial_recursive(n) :
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1) # n * (n-1)!

print("반복", factorial_iterative(5))
print("재귀", factorial_recursive(5))