# 국영수
# : 반 학생 N명의 이름과 국어, 영어, 수학 점수가 있음
# : 학생의 성적 정렬하기
# - 국어 점수가 감소하는 순서
# - 국어 점수가 같으면 영어 점수가 증가
# - 국어, 영어가 같으면 수학 점수 감소
# - 모든 점수가 같으면 이름이 사전 순으로 증가 (아스키코드에서 대문자가 더 앞으로 온다)

n = int(input())
name = []

for i in range(n) :
    name.append(input().split())

name.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in name :
    print(i[0])