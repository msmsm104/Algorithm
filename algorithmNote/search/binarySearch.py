# binarySearch.py
# 이진 탐색
# 조건 : 내부의 데이터가 정렬되어 있을때 사용 가능.
# 탐색 범위를 절반씩 좁혀가며 탐색 (변수 : 시작점, 끝점, 중간점)
# 시간 복잡도 O(logN)

# 재귀 함수로 구현
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점의 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은경우
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    
# 반복문으로 구현
def binary_search_2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은경우  중간점의 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은경우
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    return None

# 입력값
n = 10
target = 7
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

result = binary_search_2(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

