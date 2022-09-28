# 윤년
# : 4로 나누어 떨어지는 해는 윤년
# : 100으로 나누어떨어지고, 400으로 떨어지지 않는 해는 윤년이 아님

num = int(input())

def year (n) :
    if n % 4 == 0 :
        if (n % 100 == 0) & (n % 400 != 0) :
            return False
        return True
    return False

print(year(num))