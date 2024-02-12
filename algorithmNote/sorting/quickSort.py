# quickSort.py
# 퀵 정렬
import random
import time
# 기준을 설정한 다음 큰 수와 작은 수를 교환환 후 리스트를 반으로 나누는 방식으로 동작

# 기준 - pivot
# 분할 방식에 따라 종류가 여러가지로 나뉨
# 호어 분할 (Hoare Partition)
    # 리스트에서 첫 번째 데이터를 피벗으로 정한다.

array = [random.randint(1,100) for _ in range(10000)]
print(array[:20])


def quickSort(array, start_idx, end_idx):
    # 원소가 1개인 경우 종료 - 재귀함수 종료조건
    if start_idx >= end_idx:
        return
    pivot = start_idx # 피벗을 첫번째 원소로 지정
    left = start_idx + 1
    right = end_idx

    # 교차하기 전까지 반복
    while left <= right:
        # 왼쪽에서는 피벗 보다 큰 수를 찾을때까지 left + 1 반복
        while left <= end_idx and array[left] <= array[pivot]:
            left += 1
        # 오른쪽에서는 피벗보다 작은 수를 찾을때까지 right - 1 반복
        while right > start_idx and array[right] >= array[pivot]:
            right -= 1
        # left, right 가 엇갈리는 경우 작은수와 큰수를 교체
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
        
    # 분할 이후 
    quickSort(array, start_idx, right - 1)
    quickSort(array, right + 1, end_idx)

def quickSort_2(array):
    # 리스트가 하나 이하의 원소만을 담을경우 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행, 전체 리스트 반환
    return quickSort_2(left_side) + [pivot] + quickSort_2(right_side)


start_time = time.time()
quickSort(array, 0, len(array) - 1)
end_time = time.time()
print(array[:20])
print(f"퀵 정렬 시간 : {end_time - start_time}")

array = [random.randint(1,100) for _ in range(10000)]
print(array[:20])

start_time = time.time()
array = quickSort_2(array)
end_time = time.time()
print(array[:20])
print(f"퀵 정렬 시간 : {end_time - start_time}")