# countSort.py
# 계수정렬

# 1. 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있도록 하나의 리스트를 생성
# 2. 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있도록 하나의 리스트를 생성
idx_array = [0 for _ in range(max(array) + 1)]

# 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가
for i in array:
    idx_array[i] += 1

# 결과값을 배열로 반환할 경우
result = []

for i in range(len(idx_array)):
    for _ in range(idx_array[i]):
        result.append(i)
        print(i, end = " ")

print(result)


