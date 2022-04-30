# 톱니바퀴

# 총 8개의 톱니를 가지고 있는 톱니바퀴 4개
# 톱니는 N극 또는 S극 중 하나를 나타내고 있다.
# 가장 왼쪽 1번, 그 오른쪽은 2번, 그 오른쪽은 3번, 가장 오른쪽 4번

# 톱니바퀴를 총 K번 회전시키려고 한다.
# 톱니바퀴의 회전은 한 칸을 기준으로 한다.
# 회전은 시계 방향과 반시계 방향

# 서로 맞닿은 톱니의 극이 다르다면, 회전한 방향과 반대방향
# 맞닿은 톱니의 극이 같다면, 회전 X

# 톱니바퀴의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때,
# 최종 톱니바퀴의 상태를 구하는 프로그램

# 총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력한다.
    # 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
    # 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
    # 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
    # 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점

# N극은 0, S극은 1
# 1은 시계, -1은 반시계



# def turn(k, vehicle, info) :
#     for i in range(k) :
#         if info[i][0] == 1 :
#             if vehicle[0][2] == vehicle[1][6] :
#                 if info[i][1] == -1 :   # 반시계
#                     vehicle[0] = vehicle[0][1:8] + [vehicle[0][0]]
#                 elif info[i][1] == 1 :  # 시계
#                     vehicle[0] = [vehicle[0][7]] + vehicle[0][0:7]
#             else :
#                 if info[i][1] == -1 :
#                     vehicle[0] = vehicle[0][1:8] + [vehicle[0][0]]  # 반시계
#                     vehicle[1] = [vehicle[1][7]] + vehicle[1][0:7]  # 시계
#                 elif info[i][1] == 1 :
#                     vehicle[0] = [vehicle[0][7]] + vehicle[0][0:7]  # 시계
#                     vehicle[1] = vehicle[1][1:8] + [vehicle[1][0]]  # 반시계
#
#         elif info[i][0] == 2 :
#             if vehicle[1][2] == vehicle[2][6] :
#                 if info[i][1] == -1 :   # 반시계
#                     vehicle[1] = vehicle[1][1:8] + [vehicle[1][0]]
#                 elif info[i][1] == 1 :  # 시계
#                     vehicle[1] = [vehicle[1][7]] + vehicle[1][0:7]
#             else :
#                 if info[i][1] == -1 :
#                     vehicle[1] = vehicle[1][1:8] + [vehicle[1][0]]  # 반시계
#                     vehicle[2] = [vehicle[2][7]] + vehicle[2][0:7]  # 시계
#                 elif info[i][1] == 1 :
#                     vehicle[1] = [vehicle[1][7]] + vehicle[1][0:7]  # 시계
#                     vehicle[2] = vehicle[2][1:8] + [vehicle[2][0]]  # 반시계
#
#         elif info[i][0] == 3 :
#             if vehicle[2][2] == vehicle[3][6] :
#                 if info[i][1] == -1 :   # 반시계
#                     vehicle[2] = vehicle[2][1:8] + [vehicle[2][0]]
#                 elif info[i][1] == 1 :  # 시계
#                     vehicle[2] = [vehicle[2][7]] + vehicle[2][0:7]
#             else :
#                 if info[i][1] == -1 :
#                     vehicle[2] = vehicle[2][1:8] + [vehicle[2][0]]  # 반시계
#                     vehicle[3] = [vehicle[3][7]] + vehicle[3][0:7]  # 시계
#                 elif info[i][1] == 1 :
#                     vehicle[2] = [vehicle[2][7]] + vehicle[2][0:7]  # 시계
#                     vehicle[3] = vehicle[3][1:8] + [vehicle[3][0]]  # 반시계
#
#         elif info[i][0] == 4 :
#             if vehicle[3][6] == vehicle[2][2] :
#                 if info[i][1] == -1 :   # 반시계
#                     vehicle[3] = vehicle[3][1:8] + [vehicle[3][0]]
#                 elif info[i][1] == 1 :  # 시계
#                     vehicle[3] = [vehicle[3][7]] + vehicle[3][0:7]
#             else :
#                 if info[i][1] == -1 :
#                     vehicle[3] = vehicle[3][1:8] + [vehicle[3][0]]  # 반시계
#                     vehicle[2] = [vehicle[2][7]] + vehicle[2][0:7]  # 시계
#                 elif info[i][1] == 1 :
#                     vehicle[3] = [vehicle[3][7]] + vehicle[3][0:7]  # 시계
#                     vehicle[2] = vehicle[2][1:8] + [vehicle[2][0]]  # 반시계
#     return vehicle



def findgear(target, direction) :
    global gears
    res = [0] * 4

    res[target] = direction

    # 왼쪽
    for i in range(target-1, -1 ,-1) :
        if gears[i][2] == gears[i+1][6] :
            break
        res[i] = res[i+1] * -1

    # 오른쪽
    for i in range(target + 1, 4) :
        if gears[i][6] == gears[i-1][2] :
            break

        res[i] = res[i-1] * -1

    return res

def rotate(res) :
    global gears

    for i in range(4) :
        if res[i] == 0 :
            continue

        elif res[i] == 1 :
            gears[i] = [gears[i][7]] + gears[i][0:7]

        else :
            gears[i] = gears[i][1:8] + [gears[i][0]]





gears = []
info = []
for i in range(4) :
    gears.append(list(map(int, input())))

k = int(input())
for i in range(k) :
    a, b = map(int, input().split())
    info.append((a, b))

for g, d in info :
    res = findgear(g-1, d)
    rotate(res)

score = gears[0][0] + gears[1][0] * 2 + gears[2][0] * 4 + gears[3][0] * 8
print(score)











