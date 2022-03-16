# 외벽 점검
# : 레스토랑은 완전히 동그란 모양, 외벽의 총 둘레는 n 미터
# : 정북 방향 지점 0, 취약 지점의 위치는 정북방향지점으로부터 시계방향으로 떨어진 거리
# : 친구들은 출발지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동
# : 외벽의 길이 n, 취약 지점의 위치가 담긴 배열 weak, 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 dist가 매개변수로 주어질 때, 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최솟값을 return 하도록 solution


from itertools import permutations

def solution(n, weak, dist) :
    length = len(weak)
    for i in range(length) :
        weak.append(weak[i] + n)
    answer = len(dist) + 1   # 투입할 친구의 수 최솟값
    for start in range(length) :
        # 친구 나열하는 모든 경우의 수
        for friends in list(permutations(dist, len(dist))) :
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start, start + length) :
                if position < weak[index] :
                    count += 1
                    if count > len(dist) :  
                        break
                    position = weak[index] + friends[count - 1]
        answer = min(answer, count)

    if answer > len(dist) :
        return -1
    return answer