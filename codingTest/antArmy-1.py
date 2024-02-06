# antArmy-1.py

# 그리디 알고리즘
import sys
import time

# 입력값 hp - 사냥감의 체력 (int)
hp = int(sys.stdin.readline().rstrip())
ants = [5, 3, 1]

# 출력값 - 최소한의 병력수
result = 0

# hp 를 공격력으로 나누었을때
# 몫 - 해당 공격력의 개미수
# 나머지 - 남은 hp

start_time = time.time()
# 시간복잡도는 상수 O(1)
for ant in ants:
    result += hp // ant # 공격력에 대한 개미수
    hp = hp % ant

end_time = time.time()

print(f"알고리즘 성능(상수) : {end_time - start_time}")
print(result)
