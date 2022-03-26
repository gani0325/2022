# 가사 검색
# : 키워드는 와일드 카드 문자 중 하나인 ?가 포함된 패턴 형태의 문자열
# : 가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries 가 주어질 때, 각 키워드별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하는 solution

from bisect import bisect_left, bisect_right

# 값 left, right 데이터 개수 반환
def count_by_range(a, left_value, right_value) :
    right_index = bisect_right(a, right_value) 
    left_index = bisect_left(a, left_value)
    return right_index - left_index

array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution(words, queries) :
    answer = []
    for word in words :
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001) :
        array[i].sort()
        reversed_array[i].sort()

    for q in queries :
        if q[0] != '?' :
            res = count_by_range(array[len(q)], q.replace("?", "a"), q.replace("?", "z"))
        else :
            res = count_by_range(array[len(q)], q[::-1].replace("?", "a"), q[::-1].replace("?", "z"))
        answer.append(res)
    return answer