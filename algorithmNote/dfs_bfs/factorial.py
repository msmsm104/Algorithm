# factorial.py
# 점화식 표현
# f(n) = n x f(n - 1)

# 재귀적으로 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# 반복적으로 구현
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = int(input())

print("재귀적 : ", factorial_recursive(n))
print("반복적 : ", factorial_iterative(n))