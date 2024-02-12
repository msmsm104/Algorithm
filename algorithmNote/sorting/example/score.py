# score.py
# 성적이 낮은 순으로 학생 이름 출력하기
import time

# 입력값
n = 5 # int(input())
array = [("문석민", 95), ("홍길동", 80), ("이순신", 77), ("김유신", 82), ("이성계", 69)]

# 1. 내장 함수를 활용
start_time = time.time()
result = [i[0] for i in sorted(array, key = lambda x: x[-1])]
end_time = time.time()
print(f"내장 함수 성능(시간): {end_time - start_time}")

# 2. 계수 정렬 활용
n = 5 # int(input())
array = [("문석민", 95), ("홍길동", 80), ("이순신", 77), ("김유신", 82), ("이성계", 69)]

start_time = time.time()

max_score = max(array, key = lambda x: x[-1])[-1]
count = [0] * (max_score + 1)
result = []

for i in range(len(array)):
    count[array[i][-1]] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        result.append(i)

end_time = time.time()
print(f"계수정렬 성능(시간): {end_time - start_time}")