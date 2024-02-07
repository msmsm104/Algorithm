# secretCode.py

# 입력값
# cipher - 암호화된 문자열
# code - 자연수

import sys

data = sys.stdin

cipher = data.readline().rstrip()
code = int(data.readline().rstrip())

# 1. 문자열의 특징을 활용해 인덱싱 (순차탐색)
answer = ""
for i in range(code, len(cipher) + 1, code):
    # if i % code == 0: # 인덱스가 code의 배수인 경우
    answer += cipher[i - 1]
print(answer)

# 2. 점화식을 이용한 방법 (재귀함수, 반복문)
    # f(n) = f(n - code) + code
    # n = (len(cipher) // code) * code