# antArmy.py
# 그리디 알고리즘
import sys
import time

# 입력값 hp - 사냥감의 체력 (int)
hp = int(sys.stdin.readline().rstrip())
ants = [5, 3, 1]

# 출력값 - 최소한의 병력수
result = 0


start_time = time.time()
# 알고리즘 - 그리디 알고리즘
# 공격력이 큰 개미부터 차례대로 
# hp 값이 공격력 보다 작아질때까지 빼기
for ant in ants:
    while hp >= ant:
        hp -= ant
        result += 1
end_time = time.time()

print(f"알고리즘 성능(hp): {end_time - start_time}")
print(result)
