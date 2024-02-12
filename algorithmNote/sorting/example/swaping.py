# swaping.py

import time
import random

# 입력값 n - n개의 원소를 가지는 배열, k - k번 바꿔치기 가능
k = random.randint(100, 10000)

array_a = [random.randint(1, 1000000) for _ in range(100000)]
array_b = [random.randint(1, 1000000) for _ in range(100000)]

# array_a = list(map(int, input().split()))
# array_b = list(map(int, input().split()))

# 1. k 번 a의 가장 작은값, b의 가장 큰 값을 교체
start_time = time.time()
for _ in range(k):
    min_idx = array_a.index(min(array_a))
    max_idx = array_b.index(max(array_b))
    array_a[min_idx], array_b[max_idx] = array_b[max_idx], array_a[min_idx]

end_time = time.time()
print(f"반복 알고리즘 성능 : {end_time - start_time}")

# print(array_a)

# 2. 정렬한 다음 [0:k] 범위를 슬라이싱 하기
array_a = [random.randint(1, 1000000) for _ in range(100000)]
array_b = [random.randint(1, 1000000) for _ in range(100000)]

start_time = time.time()
array_a.sort()
array_b.sort(reverse=True)

# 첫 번째 인덱스부터 확인하며 비교 최대 k번 비교
for i in range(k):
    # 더 작은 경우에만 교체
    if array_a[i] < array_b[i]:
        array_a[i], array_b[i] = array_b[i], array_a[i]
    else:
        break
end_time = time.time()
print(f"정렬 알고리즘 성능 : {end_time - start_time}")