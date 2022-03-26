# 다이나믹
# : 큰 문제를 작은 문제로 나눈다
# : 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일
# : 큰문제에서 작은문제 => 탑다운
# : 작은 문제에서 차근차근 답 도출 => 보텀업
# : O(N)



# 피보나치
def fibo(x) :
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))



# 피보나치 + 재귀적
d = [0] * 100

def fibo(x) :
    if x == 1 or x == 2 :
        return 1
    # 계산 했던 애
    if d[x] != 0 :
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))




# 피보나치 + 호출되는 함수 확인
d = [0] * 100

def pibo(x) :
    print('f(', str(x), ')', end = " ")
    if x == 1 or x == 2 :
        return 1
    if d[x] != 0  :
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]
pibo(5)





# 피보나치 + 반복적
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1) :
    d[i] = d[i-1] + d[i-2]
print(d[n])



