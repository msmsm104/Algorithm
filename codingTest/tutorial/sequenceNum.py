# sequenceNum.py
# 연속된 수의 합

# 입력값 - 연속된 num개의 수를 더해 total이 되는 수
num = 4
total = 14

# n + (n + 1) + (n + 2)... (n + (num - 1)) = total
# (n * num) + (0 + 1 + 2... + (num - 1))
# {total - (0 + ... + (num - 1))} / num = n

# 시간 복잡도 O(N)
def solution(num, total):
    total_num = 0
    # O(N)
    for i in range(num):
        total_num += i

    answer = int((total - total_num) / num)

    result = []
    # O(N)
    for i in range(num):
        result.append(answer + i)

    return result


