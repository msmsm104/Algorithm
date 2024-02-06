# two-point algorithm
# 특정 합을 가지는 부분 연속 수열 찾기

import sys

# input_data = sys.stdin

# 입력값 n - 데이터의 갯수
# 입력값 m - 찾고자 하는 부분 합
n, m = map(int, sys.stdin.readline().rstrip().split())

# 입력값 data - 전체 수열
data = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)