# rcp.py
# 가위 바위 보

import sys

# 입력값
# 2 - 가위, 0 - 바위, 5 - 보
rsp = sys.stdin.readline().rstrip()

# 자료구조
dict = {
    "2": "0",
    "0": "5",
    "5": "2"
}

# 알고리즘 (순차탐색)
result = ""

for value in rsp:
    result += dict[value]

print(result)


