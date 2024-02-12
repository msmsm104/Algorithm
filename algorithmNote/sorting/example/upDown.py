# upDown.py

import random
import time

# 가장 빠르게 해결할 수 있는 것은 계수정렬을 구현하는 방식이라고 생각한다.

# 1. 내장 함수를 활용하는 방법
# 2. 계수정렬 방식을 활용

# 입력값
# n = int(input())
# array = []

# for _ in range(n):
#     data = int(input())
#     array.append(data)
array = [random.randint(1, 100000) for _ in range(500)]



# 1. 내장 함수를 활용하는 방법
start_time = time.time()
result = sorted(array, reverse=True)
end_time = time.time()
print(f"내장 함수 시간 : {end_time - start_time}")


array = [random.randint(1, 100000) for _ in range(500)]

# 2. 계수정렬
start_time = time.time()

count = [0] * (max(array) + 1)
result= []

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for _ in range(count[i]):    
        result.append(i)

result.reverse()
# print(result)

end_time = time.time()
print(f"계수정렬 시간 : {end_time - start_time}")
