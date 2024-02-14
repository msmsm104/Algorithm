# countOfK.py

import random
import time

# 입력값 - i ~ j 까지 k 가 몇번 등장하는지
i = 10
j = 10000000
k = random.randint(0, 9)


# 내장 함수를 이용해서 구현
def countK_1(i, j, k):
    array = []

    for x in range(i, j + 1):
        for y in list(str(x)):
            array.append(y)
        # print(list(str(x)), end = " ")
    return array.count(str(k))

# 계수정렬을 이용한 탐색
def countK_2(i, j, k):
    count = [0] * 10

    for x in range(i, j + 1):
        for y in list(str(x)):
            count[int(y)] += 1

    return count[k]


start_time = time.time()
result = countK_1(i, j, k)
print(result)
end_time = time.time()
print(f"내장 함수 성능 : {end_time - start_time}")

start_time = time.time()
result = countK_2(i, j, k)
print(result)
end_time = time.time()
print(f"계수정렬 성능 : {end_time - start_time}")


