# searchPart.py
# 부품찾기

# 입력값
n = 5
n_array = [8, 3, 7, 9, 2]
m = 3
m_array = [5, 7, 9]

# 순차탐색 sequential search
def sequentialSearch(n_array, target):
    for i in range(len(n_array)):
        if n_array[i] == target:
            return i

for j in range(len(m_array)):
    result = sequentialSearch(n_array, m_array[j])
    if result == None:
        print("no")
    else:
        print("yes")



# 이진탐색 binary search(재귀, 반복)
def binarySearch(array, target, start, end):
    if start > end:
        return None
    # 중간값 설정
    mid = (start + end) // 2
    # 중간값과 타켓이 동일한 경우
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearch(array, target, start, mid - 1)
    elif array[mid] < target:
        return binarySearch(array, target, mid + 1, end)
    
def binarySearch_2(array, target, start, end):
    while start <= end:
        # 중간값 설정
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    return None

for j in range(len(m_array)):
    result = binarySearch(n_array, m_array[j], 0, len(n_array) - 1)
    if result == None:
        print("no")
    else:
        print("yes")

for j in range(len(m_array)):
    result = binarySearch_2(n_array, m_array[j], 0, len(n_array) - 1)
    if result == None:
        print("no")
    else:
        print("yes")