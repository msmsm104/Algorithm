# lines.py
# 겹치는 선분의 길이

# 입력값
lines = [[0, 5], [3, 9], [1, 10]]

# 출력값
result = 0

# 2개이상 겹치는 선분 길이의 합
print([max(lines[0][0], lines[1][0]), min(lines[0][1], lines[1][1])])
print([max(lines[0][0], lines[2][0]), min(lines[0][1], lines[2][1])])
print([max(lines[1][0], lines[2][0]), min(lines[1][1], lines[2][1])])

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        print([max(lines[i][0], lines[j][0]), min(lines[i][1], lines[j][1])])
        print(min(lines[i][1], lines[j][1]) - max(lines[i][0], lines[j][0]))