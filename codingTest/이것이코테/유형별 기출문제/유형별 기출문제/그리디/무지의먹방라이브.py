# 무지의 먹방 라이브
# : 회전판에 먹어야 할 N개의 음식이 있다
# : 각 음식에는 1부터 N개의 번호가 붙어있고, 각 음식 섭취의 일정 소요시간이 잇다
# 1) 1번부터 먹으며, 번호가 증가하는 순서대로 음식이 앞으로 온다
# 2) 마지막 번호 음식 섭취 후, 다시 1번 음식이 앞으로 온다
# 3) 음식 하나를 1초 동안 헙취한 후 남은 음식은 두고, 다음 음식 섭취
# (다음 음식이란 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식)
# 4) 회전판이 음식을 앞으로 가져오는데 걸리는 시간이 없다고 가정
# : 먹방 시작한지 K초 후에 장애로 방송 잠시 중단
# : 다시 정상화 후, 몇 번 음식부터 섭취해야 하는지 알고자 한다
# : 각 음식을 모두 먹는데 필요한 시간이 담겨 있는 배열 food_times
# : 네트워크 장애가 발생한 시간 k초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수 완성

import heapq

def solution(food_times, k) :
    if sum(food_times) <= k :
        return -1

    q = 0
    for i in range(len(food_times)) :
        heapq.heappush(q, (food_times[i], i+1))  # 음식시간, 음식 번호
    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k :
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    result = sorted(q, key = lambda x : x[1]) # 음식 번호로
    return result[(k - sum_value) & length[1]]


