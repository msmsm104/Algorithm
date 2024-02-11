# selectionSort.py
# 선택 정렬 알고리즘

# "매번 가장 작은것을 선택한다"

import random

array = [random.randint(1, 100) for _ in range(100)]


# 선택 정렬 알고리즘
def selectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    
    return array

selectionSort(array)

print(array[:20])
