# 선형검색
# 원하는 값 찾기

num_list = [23, 12, 55, 32, 45, 76, 88, 52]

def linear (n) :
    for i in num_list :
        if i == n :
            return True
    return False

print(linear(5))

# result
# False