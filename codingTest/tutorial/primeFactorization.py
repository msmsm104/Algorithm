# primeFactorization.py
# 소인수 분해 문제



# 특정 숫자가 소수인지 아닌지 판별
# for i in range(1, 10001):
#     count = 0
#     for j in range(1, i  + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i, end = " ")

def isPrimeNum(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count == 2:
        return True
    return False

# 소인수분해 함수 정의
def primeFactorization(number):
    result = []
    for i in range(2, number + 1):
        while isPrimeNum(i) and number % i == 0:
            number = number // i
            result.append(i)
    return result

# print(primeFactorization(420))
        
