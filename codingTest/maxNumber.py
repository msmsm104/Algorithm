# maxNumber.py
# 가장 큰 수, 그 수의 인덱스를 반환
import sys
import time
import random

# 입력값 - 정수 배열 - 자료구조
# array = list(map(int, sys.stdin.readline().rstrip().split()))
array = [random.randint(0, 1000) for _ in range(1000)]


start_time = time.time()
# 가장 큰 수와 그 원소의 인덱스
# 1. 반복문
max_idx = -1
max_value = -1
for idx in range(len(array)):
    # 최소값 비교, 최소 인덱스값 갱신
    if array[idx] > max_value:
        max_idx = idx
        max_value = array[idx]

print(max_value, max_idx)
end_time = time.time()
print(f"수행시간 : {end_time - start_time}")
    

# 2. 내장함수
start_time = time.time()

print(max(array), array.index(max(array)))

end_time = time.time()
print(f"수행시간 : {end_time - start_time}")



# 3. 정렬
import heapq

q = []

start_time = time.time()


for i in range(len(array)):
    heapq.heappush(q, (-array[i], i))

value, index = heapq.heappop(q)
print(-value, index)
end_time = time.time()
print(f"수행시간 : {end_time - start_time}")



