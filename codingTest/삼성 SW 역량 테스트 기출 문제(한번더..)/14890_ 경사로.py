# 경사로

# 크기가 N×N인 지도가 있다. 지도의 각 칸에는 그 곳의 높이가 적혀져 있다.
# 오늘은 이 지도에서 지나갈 수 있는 길이 몇 개 있는지 알아보려고 한다.
#     길이란 한 행 또는 한 열 전부를 나타내며, 한쪽 끝에서 다른쪽 끝까지 지나가는 것

# 길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 모두 같아야 한다.
# 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다.
# 경사로는 높이가 항상 1이며, 길이는 L이다.
# 개수는 매우 많아 부족할 일이 없다. 경사로는 낮은 칸과 높은 칸을 연결하며, 아래와 같은 조건을 만족
#     경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
#     낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
#     경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다

# 아래와 같은 경우에는 경사로를 놓을 수 없다.
#     경사로를 놓은 곳에 또 경사로를 놓는 경우
#     낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
#     낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
#     경사로를 놓다가 범위를 벗어나는 경우


# 지도가 주어졌을 때, 지나갈 수 있는 길의 개수를 구하는 프로그램을 작성

# 첫째 줄에 N (2 ≤ N ≤ 100)과 L (1 ≤ L ≤ N)이 주어진다.
# 둘째 줄부터 N개의 줄에 지도가 주어진다.
#     각 칸의 높이는 10보다 작거나 같은 자연수이다.

# 첫째 줄에 지나갈 수 있는 길의 개수를 출력


# 배열 길이, 경사로 길이
N, L = map(int, input().split())
graph = []
for i in range(N) :
    graph.append(list(map(int, input().split())))
case = []   # 지날 수 있는 길의 경우들
count = 0   # 가능한 길

def check(l) :
    pre = l.pop()   # 이전 땅 높이
    extra = [pre]   # 경사로 놓을 수 있는 여분 땅

    while l :       # 다음 땅이 남아 있다면
        next = l.pop()

        if pre == next :     # 이전 땅과 높이 같음.
            extra.append(next)
        elif pre == next - 1 :  # 현재가 이전보다 한칸 높음
            # 경사로 길이만큼 이전 땅이 개수가 있어야됨
            for k in range(L) :
                if len(extra) < L :     # 적다면 xx
                    return False
            extra.clear()           # 이전땅 이제 불가
            extra.append(next)      # 다음땅 넣기
        elif pre == next + 1 :  # 현재가 이전보다 한칸 낮음
            for k in range(L - 1) :
                if not l or l.pop() != next :   # 경사도 길이보다 적고, 모두 높이가 다르다면
                    return False
            extra.clear()
        else :
            return False
        pre = next
    return True    

for i in range(N) :
    cardi = []     # 열
    for j in range(N) :
        cardi.append(graph[j][i])
    case.append(graph[i][:])        # 행
    case.append(cardi[:])
# 행열, 행열, 행열~~~~
# print(case)

# 경사로 이용해서 가능한지~ 확인
for i in case :
    if check(i) :
        count += 1

print(count)

# input
# 6 2
# 3 2 1 1 2 3
# 3 2 2 1 2 3
# 3 2 2 2 3 3
# 3 3 3 3 3 3
# 3 3 3 3 2 2
# 3 3 3 3 2 2

# output
# 7