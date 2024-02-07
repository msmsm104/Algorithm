# time.py

# 완전 탐색 알고리즘
# 시,분,초에 해당하는 값을 삼중 반복문으로 구현

# 입력값 N - 시간 (0 <= N <= 23)
n = int(input())

result = 0

# 알고리즘 (완전 탐색 알고리즘)
for hour in range(n + 1):
    for min in range(0, 60):
        for sec in range(0, 60):
            if "3" in str(hour) + str(min) + str(sec):
                result += 1

print(result)