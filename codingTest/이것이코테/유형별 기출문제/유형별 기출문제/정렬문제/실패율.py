# 실패율
# : 실패율은 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
# : 전체 스테이지 개수 N, 게임ㅇ르 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨져 있는 배열을 return 하는 solution
# : 실패율이 높은 스테이지부터 본호 출력

def solution(N, stages) :
    answer = []
    length = len(stages)

    for i in range(1, N+1) :
        # 스테이지에 머물러 있는 사람 수
        count = stages.count(i)

        # 실패율 계산
        if length == 0:
            fail = 0
        else :
            fail = count / length

        answer.append((i, fail))     # 스테이지 번호, 실패율
        length -= count
    answer = sorted(answer , key = lambda t : t[1], reverse = True)
    answer = [i[0] for i in answer]
    return answer