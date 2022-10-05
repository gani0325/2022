# 깊이 우선 탐색
# 주로 재귀 사용


# # 1) 전위 순회를 이용한 탐색
# tree = [[1, 2], [3, 4], [5, 6], [7, 8], [ 9, 10], [11, 12], [13, 14],
# [], [], [], [], [], [], [], []]     # 빈 리스트는 각 노드의 탐색 결과를 저장할 영역을 확보하려는 것

# def search(pos) :
#     print(pos, end = " ")       # 자식 노드를 탐색하기 전에 현재 노드 출력
#     for i in tree[pos] :        # 자식 노드 탐색
#         search(i)               # 재귀 탐색

# search(0)

# # result
# # 0 1 3 7 8 4 9 10 2 5 11 12 6 13 14


# # 2) 후위 순회를 이용한 탐색
# tree = [[1, 2], [3, 4], [5, 6], [7, 8], [ 9, 10], [11, 12], [13, 14],
# [], [], [], [], [], [], [], []]     # 빈 리스트는 각 노드의 탐색 결과를 저장할 영역을 확보하려는 것

# def search(pos) :
#     for i in tree[pos] :        # 자식 노드 탐색
#         search(i)               # 재귀 탐색
#     print(pos, end = " ")       # 자식 노드 탐색 후 출력        

# search(0)

# # result
# # 7 8 3 9 10 4 1 11 12 5 13 14 6 2 0 

# # 3) 중위 순회를 이용한 탐색
# tree = [[1, 2], [3, 4], [5, 6], [7, 8], [ 9, 10], [11, 12], [13, 14],
# [], [], [], [], [], [], [], []]     # 빈 리스트는 각 노드의 탐색 결과를 저장할 영역을 확보하려는 것

# def search(pos) :
#     if len(tree[pos]) == 2 :        # 자식 노드가 2개 있을 때
#         search(tree[pos][0])
#         print(pos, end = " ")       # 왼쪽 노드와 오른쪽 노드 사이에 출력
#         search(tree[pos][1])
#     elif len(tree[pos]) == 1 :      # 자식 노드가 1개 있을 때
#         search(tree[pos][0])
#         print(pos, end = " ")
#     else :
#         print(pos, end = " ")

# search(0)

# # result
# # 7 3 8 1 9 4 10 0 11 5 12 2 13 6 14 

# 4) 재귀 사용 없이 while, for 사용
tree = [[1, 2], [3, 4], [5, 6], [7, 8], [ 9, 10], [11, 12], [13, 14],
[], [], [], [], [], [], [], []]     # 빈 리스트는 각 노드의 탐색 결과를 저장할 영역을 확보하려는 것

data = [0]

def search(pos) :
    if len(tree[pos]) == 2 :        # 자식 노드가 2개 있을 때
        search(tree[pos][0])
        print(pos, end = " ")       # 왼쪽 노드와 오른쪽 노드 사이에 출력
        search(tree[pos][1])
    elif len(tree[pos]) == 1 :      # 자식 노드가 1개 있을 때
        search(tree[pos][0])
        print(pos, end = " ")
    else :
        print(pos, end = " ")

search(0)

# result
# 7 3 8 1 9 4 10 0 11 5 12 2 13 6 14 