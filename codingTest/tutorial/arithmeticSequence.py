# arithmeticSequence.py
# 등차, 등비수열

# 입력값
common = [1,2,3,4]

# 출력값 - 다음에 오는 숫자
def solution(common):
    answer = 0

    # 등차수열 여부 확인
    minus_value = 0
    if common[1] - common[0] == common[2] - common[1]:
        # 등차수열
        answer = common[-1] + (common[1] - common[0])
    else:
        # 등비수열
        answer = common[-1] * (common[1] / common[0])
    return answer