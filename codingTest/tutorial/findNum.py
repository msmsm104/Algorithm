# findNum.py
# 합성수 찾기

# 합성수 - 약수의 개수가 세 개 이상인 수

# 입력값 - n
n = int(input())

# 자연수 n의 약수의 갯수를 반환하는 함수 정의
def findNum(num):
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 2
            if i ** 2 == num:
                count -= 1
    
    return count

# 자연수 n이하의 자연수에 대해 합성수의 갯수
def findCol(num):
    count = 0
    for i in range(1, num + 1):
        if findNum(i) >= 3:
            count += 1
    return count

print(findCol(n))