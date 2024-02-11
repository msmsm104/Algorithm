# height.py
import random
import time
## 머쓱이 보다 키 큰 사람

# 입력값 - 배열(키), 머쓱이의 키
array = [random.randint(150, 190) for _ in range(1000000)]
height = random.randint(150, 190)

# 출력값 - 머쓱이 보다 큰 키를 가진 사람 수

print(f"목표값 : {height}")

# 알고리즘 - 순차(완전 탐색)
start_time = time.time()
count = 0

for h in array:
    if h > height:
        count += 1

print(count)

end_time = time.time()
print(f"1 알고리즘 성능 : {end_time - start_time}")

# 2. 알고리즘 - 정렬
start_time = time.time()

array.append(height)

array.sort()

idx = array.index(height)
same_num = array.count(height)
result = len(array) - (idx + 1) - same_num + 1

print(result)

end_time = time.time()
print(f"2 알고리즘 성능 : {end_time - start_time}")


