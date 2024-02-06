# eratosthenes.py
# 에라토스테네스의 체

# n 보다 작거나 같은 모든 소수를 찾을 때 활용되는 알고리즘

import math

n = 1000 # 2 부터 1000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인 => 가운데 약수를 기준으로 대칭구조를 가지기 때문에 제곱근까지만 확인하면 된다.
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end = " ")