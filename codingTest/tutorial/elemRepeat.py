# elemRepeat.py
# 중복되는 원소의 갯수

import random
import time

array = [1, 1, 2, 3, 4, 5]
n = 1

# 내장 함수
result = array.count(n)
print(result)

# 순차 탐색
result = 0
for i in range(len(array)):
    if array[i] == n:
        result += 1
print(result)


