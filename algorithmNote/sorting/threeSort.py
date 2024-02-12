# threeSort.py
import random
import time

# 선택 정렬, 삽입 정렬, 퀵 정렬
sample_array = [random.randint(1, 100) for _ in range(20)]

# 선택 정렬
# 항상 가장 작은 수를 선택하여 반환
def selectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

# 삽입 정렬
# 배열의 두번째 원소부터 시작하여 이미 정렬되어 졌다고 가정한 원소들과 차례로 비교, 더 작은값이 나오는 경우 해당 위치에 삽입
def insertionSort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]: # 한칸씩 옆으로 가면서 비교
                array[j], array[j - 1] = array[j - 1], array[j] 
            else:
                break # 더 작은 값을 만나면 그 위치에서 멈춤
    return array

# 퀵 정렬
# pivot 설정
# 왼쪽에서부터 pivot보다 큰값, 오른쪽에서 부터 pivot 보다 작은 값 위치 교환
def quickSort(array, start, end):
    # 종료 조건 - 원소가 1개인 경우
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    # 교차하기 전까지 반복
    while left <= right:

        # 왼쪽에서 부터 큰값 탐색
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 오른쪽에서 부터 작은 값 탐색
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    
    quickSort(array, start, right - 1)
    quickSort(array, right + 1, end)

# 퀵 정렬  - 구현 2
def quickSort_2(array):
    # 종료 조건
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quickSort_2(left_side) + [pivot] + quickSort_2(right_side)

array = quickSort_2(sample_array)
print(array)
