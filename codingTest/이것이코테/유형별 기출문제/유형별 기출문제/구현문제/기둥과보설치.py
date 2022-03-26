# 기둥과 보 설치
# : 기둥과 보를 이용하여 벽면 구조물을 자동으로 세우는 로봇을 개발
# : 2차원 가상 벽면에 기동과 보를 이용한 구조물 설치
# : 기둥과 보는 길이가 1인 선분으로 표현되며
# - 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 다른 기둥 위에 있어야 한다
# - 보는 한쪽 끝부분이 기둥 위에 있거나, 양쪽 끝부분이 다른 보와 동시에 연결되어야 함
# : 2차원 벽면은 n X n 정사각 격자 형태, 각 격자는 1x1

# 설치된 구조물이 가능한지
def possible(answer)  :
    for x, y, stuff in answer :
        if stuff == 0 :  # 기둥 설치
            # 바닥위, 한쪽 끝부분 위, 다른 기둥 위
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y -1 , 0] in answer :
                continue
            return False
        
        elif stuff == 1 : # 설치된게 보
            # 한쪽 끝부분이 기둥 위, 양쪽 끝부분이 다른 보와 동시에 연결
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer ) :
                continue
            return False

    return True


def solution(n, build_frame) :
    answer = []
    for frame in build_frame :
        x, y, stuff, operate = frame
        if operate == 0 : # 삭제
            answer.remove([x, y, stuff])
            # 가늗한 구조물인지
            if not possible(answer) :
                answer.append([x, y, stuff]) # 아니라면 다시 설치
        if operate == 1 : # 설치
            answer.append([x, y, stuff])
            if not possible(answer) :
                answer.remove([x, y ,stuff]) # 아니라면 다시 제거
    return sorted(answer)

  
    

      