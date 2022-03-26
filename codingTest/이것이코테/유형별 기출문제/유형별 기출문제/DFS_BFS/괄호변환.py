# 괄호변환
# : 소스코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램을 개발
# : (와 )의 개수가 같다면 균형잡힌 괄호 문자열
# : (와 )의 괄호의 짝도 같다면 올바른 괄호 문자열
# - 입력이 빈 문자열. 반환
# - 문자열 w를 균형잡힌 괄호 문자열 u, v로 구분한다
# : 문자열을 u에 붙인 후 반환
# => 균형잡힌 괄호 문자열 p가 주어지면 올바른 괄호 문자열로 반환 return 하는 solution 함수 ㄱ 

def balanced_index(p) :
    count = 0
    for i in range(len(p)) :
        if p[i] == '(' :
            count += 1
        else :
            count -= 1
        if count == 0 :
            return i

def check_proper(p) :
    count = 0 # left
    for i in p :
        if i == "(" :
            count += 1
        else :
            if count == 0 :
                return False
            count -= 1
    return True

def solution(p) :
    answer = ''
    if p == '' :
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if check_proper(u) :
        answer - u + solution(v)
    else :
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])

        for i in range(len(u)) :
            if u[i] == '(' :
                u[i] == ')'
            else :
                u[i] == '('
        answer += "".join(u)
    return answer