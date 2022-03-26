# 문자열 압축
# : 압축할 문자열 s가 매개변수로 주어질 때, 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수 완성

def solution(string) :
    answer = len(string)

    for i in range(1, answer // 2 + 1) :
        compressed = ""
        prev = string[0:i] # 앞에서 i만큼 문자열 추출
        count = 1

        for j in range(i, answer, i) :
            if prev == string[j:j + i] :
                count += 1
            else :
                compressed += str(count) + prev if count >= 2 else prev
                prev = string[j:j + i]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer

