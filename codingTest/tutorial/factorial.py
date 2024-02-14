# factorial.py
# 팩토리얼


# 입력값 - 자연수 n (0 < n <= 3,628,800)
n = int(input())

# 출력값 - i! <= n를 만족하는 i를 반환


# 팩토리얼 알고리즘
# 점화식 f(n) = n * f(n - 1), f(1) = 1

# 팩토리얼 함수 정의
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def solution(n):
    result = 1

    while factorial(result) <= n:
        result += 1
    
    return result - 1

print(solution(n))

