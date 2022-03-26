# 카드 정렬하기
# : 정렬된 두 묶음의 숫자 카드가 있을 때, 각 묶음의 카드 수를 A, B
# : 두 묶음을 합쳐 하나로 만드는 데 A + B 번의 비교 필요
# : N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지 구하라
# : 항상 작은 크기의 두 카드 묶음을 햡쳤을 때 최적의 해 보장!! 
# : 가장 작은 크기의 두 카드 묶음을 합치면 됨 (그리디 알고리즘 가능)
# : 우선순위 큐를 이용하여!! 

import heapq

n = int(input())
heap = []
for i in range(n) :
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1 :
    # 가장 작은 2개
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음 합쳐서 다시 삽입
    sum = one + two
    result += sum
    heapq.heappush(heap, sum)

print(result)
