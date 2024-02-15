# binaryNum.py
# 이진수 더하기 문제


# 알고리즘
# 1. 이진수 => 십진수 => 십진수 합산 => 이진수로 변환
# 2. 이진수 더하는 내장 함수 활용

# 입력값 - n : "1001"
n = input("이진수를 입력하세요 : ")

# 이진수 -> 십진수 함수 정의
def binaryToDecimal(strNum):
    result = 0

    for i in range(len(strNum)):
        result += (2 ** (len(strNum) - (i + 1))) * int(strNum[i])
    
    return result

def decimalToBinary(num):
    count = 0
    while num != 0:
        n = 0
        while 2 ** n <= num:
            n += 1
        n -= 1

        num -= 2 ** n

        if count == 0:
            result = [0] * (n + 1)
            count += 1
        result[n] += 1

    result.reverse()
    # print(result)
    return "".join(map(str, result))


# 이진수 더하기 함수 정의
def solution(bin1, bin2):
    n, m = binaryToDecimal(bin1), binaryToDecimal(bin2)
    # print(n , m)
    decimal_num = n + m

    result = decimalToBinary(decimal_num)

    return result

print(solution("1001010010", "1111"))

# print(decimalToBinary(24))

### 결과값 - 런타임 에러 나오는 test case 가 존재한다.
### 단순하게 자릿수 계산만으로 해결 가능할것으로 생각.