# traveler.py

import sys
# 입력값 N - 공간의 크기
# 입력값 A - 이동 계획서
data = sys.stdin

n = int(data.readline().rstrip())
plans = list(data.readline().rstrip().split())

# 시뮬레이션 알고리즘
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# moves_type = ["U", "D", "L", "R"]
moves_type = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

x, y = 1, 1

for plan in plans:
    # for j in range(len(moves_type)):
    #     if i == moves_type[j]:
    #         nx = x + dx[j]
    #         ny = y + dy[j]
    nx = x + moves_type[plan][0]
    ny = y + moves_type[plan][-1]
    if nx >=1 and nx <= n and ny >=1 and ny <= n: # 공간을 벗어나지 않는 경우에만 값을 갱신
        # x = nx
        # y = ny
        x, y = nx, ny
    
print(x, y)