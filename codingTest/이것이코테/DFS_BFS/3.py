# 1. 음료수 얼려먹기
# : N X M 크기의 얼음틀
# : 구멍이 뚫린 부분은 0, 칸막이는 1
# : 생성되는 아이스크림의 개수 구하기 (0으로 이어진 애들)

# DFS로 접근
# - 상, 하, 좌, 우 주변에 값이 0이면서 아직 방문하지 않은 지점 방문
# - 방문한 지점에서 다시 방문 진행하면, 연결된 모든 지점 방문
# - 모든 노드에 반복하며 방문하지 않은 지점 수 세기

n, m = map(int, input().split())

graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

def dfs(x, y) :
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    
    # 현재 노드 아직 방문 안했다면
    if graph[x][y] == 0 :
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i,j) == True :
            result += 1
print(result)