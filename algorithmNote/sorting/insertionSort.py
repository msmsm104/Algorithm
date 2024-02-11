# insertionSort.py
# 삽입정렬 알고리즘

# 2번째 원소부터 시작
# 기존에 정렬되어 있는 원소를 차례대로 비교
# 자신보다 작은 값을 만나게 되면 비교를 중단, 해당 위치에 삽입
## 배열이 거의 정렬되어 있는 상태라면 퀵정렬 보다 강력하게 동작한다.

import random

# 임의의 배열
array = [random.randint(1, 100) for _ in range(100)]

def insertionSort(array):
    for i in range(1, len(array)):
        # 역순으로 차례대로 비교 (그 전 원소들은 이미 정렬이 된 상태라 가정)
        for j in range(i, 0, -1): 
            if array[j] < array[j - 1]: # 한칸씩 이동하면서 비교
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    return array

insertionSort(array)
print(array[:20])

