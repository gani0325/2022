# 정확한 순위
# : 시험을 본 학생 N명의 성적 분실하고, 성적 비교한 결과의 일부만 가지고 있음
# : N 명의 성적은 모두 다르다
# : 성적이 낮다면 A -> B
# : 성적을 비교했을 때, 성적 순위를 정확히 알 수 있는 학생은 모두 몇명?
# : 최단 경로!! 플로이드 워셜

INF = 1e9

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1) :
    for b in range(1, n+1) :
        if a == b:
            graph[a][b]= 0

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0

for i in range(1 , n+1) :
    count = 0
    for j in range(1, n+1) :
        if graph[i][j] != INF or graph[j][i] != INF :
            count += 1
    if count == n:
        result += 1

print(result)
