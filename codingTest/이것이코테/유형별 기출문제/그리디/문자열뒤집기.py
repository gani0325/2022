# 문자열 뒤집기
# : 0과 1로만 이루어진 문자열 s
# : 문자열 s에 있는 모든 숫자를 전부 같게 만들다
# : s에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집기
# : 같게 만드는 행동의 최소 횟수는?

binary = input()

cnt0 = 0
cnt1 = 0

if binary[0] == '1' :
    cnt0 += 1
else :
    cnt1 += 1

for i in range(1, len(binary) - 1) :
    if binary[i] != binary[i+1] :
        if binary[i+1] == '1' :
            cnt0 += 1
        else :
            cnt1 += 1

print(min(cnt0, cnt1))