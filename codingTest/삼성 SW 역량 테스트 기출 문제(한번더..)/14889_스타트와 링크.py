# 스타트와 링크
# 오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다.
# 축구는 평일 오후에 하고 의무 참석도 아니다. 
# 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 
# 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

# BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 능력치를 조사했다. 
# 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 

# 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다.
# Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

# 축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 

# 첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 
# 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. 
# Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

import sys
input = sys.stdin.readline

def dfs(d, num) :
    global N, answer 

    if d == N // 2 :    # 팀 사람 수
        start, link = 0, 0

        for i in range(N) :
            for j in range(N) :
                # 팀 별마다..
                if visited[i] and visited[j] :
                    start += team[i][j]
                elif not visited[i] and not visited[j] :
                    link += team[i][j]
        answer = min(answer, abs(start-link))
    
    # 방문한팀, 안한팀 나누기
    for i in range(num, N) :
        if not visited[i] :
            visited[i] = 1
            dfs(d + 1, i + 1)
            visited[i] = 0

N = int(input())
team = []
for i in range(N) :
    team.append(list(map(int, input().split())))
answer = int(1e9)
visited = [0] * N

dfs(0, 0)
print(answer)

# input
# 6
# 0 1 2 3 4 5
# 1 0 2 3 4 5
# 1 2 0 3 4 5
# 1 2 3 0 4 5
# 1 2 3 4 0 5
# 1 2 3 4 5 0

# output
# 2