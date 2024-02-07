# kingdomNight.py

y_to = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8
}

moves = [{"x": 2, "y": 1}, 
         {"x": 2,  "y": -1},
         {"x": -2,  "y": 1},
         {"x": -2,  "y": -1},
         {"x": 1,  "y": -2},
         {"x": 1,  "y": 2},
         {"x": -1,  "y": -2},
         {"x": -1,  "y": 2}]

# 입력값 x, y
y, x = list(input())
# 열에 해당하는 값을 숫자값으로 변경
x = int(x)
y = y_to[y]

count = 0

# 움질일 수 있는 경우의수 최대 8가지 에 대한 완전 탐색 문제 (시뮬레이션)
for move in moves:
    nx = x + move["x"]
    ny = y + move["y"]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1

print(count)





