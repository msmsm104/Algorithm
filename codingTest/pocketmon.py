# pocketmon.py

# 입력값 - 포켓몬의 종류가 담긴 1차원 배열
# nums = list(map(int, input().split()))

def pocketmon(nums):
    result = 0
    # nums의 길이는 항상 짝수
    select_num = len(nums) / 2
    type_of_pocketmon = len(set(nums))

    result = min(select_num, type_of_pocketmon)

    return result

# print(pocketmon(nums))

# 내장 함수를 통해 구현
from itertools import combinations

# 주어진 리스트
lst = [3, 1, 2, 3]

def pocketmon_2(nums):
    result = 0

    k = len(nums) / 2
    # 조합 생성
    combs = combinations(nums, k)
    result = max(map(len,(map(set, combs))))

    return result