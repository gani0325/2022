# 3의 배수는 "Fizz"
# 5의 배수는 "Buzz"
# 3과 5의 공배수는 "FizzBuzz"
# 아니면 숫자

for i in range(1, 101) :
    if i % 3 == 0 :
        print("fizz", end = " ")
    elif (i % 3 == 0) & (i % 5 == 0) :
        print("FizzBuzz", end = " ")
    else :
        print(i, end = " ")


# result
# 1 2 fizz 4 5 fizz 7 8 fizz 10 11 fizz 13 14 fizz 16 17 fizz 19 20 fizz 22 23 fizz 25 26 fizz 28 29 fizz 31 32 fizz 34 35 fizz 37 38 fizz 40 41 fizz 43 44 fizz 46 47 fizz 49 50 fizz 52 53 fizz 55 56 fizz 58 59 fizz 61 62 fizz 64 65 fizz 67 68 fizz 70 71 fizz 73 74 fizz 76 77 fizz 79 80 fizz 82 83 fizz 85 86 fizz 88 89 fizz 91 92 fizz 94 95 fizz 97 98 fizz 100 