# mostFreq.py
# 최빈값 찾기


# 입력값
array = [1, 2, 3, 3, 3, 4]	

# 출력값
# 최빈값을 return, 여러개인 경우 -1을 return

def solution(array):
        
    answer = 0

    # 알고리즘
    # 계수정렬 알고리즘 활용
    min_num = min(array)
    max_num = max(array)
    count_array = [0] * (max_num + 1)

    # 각 계수별 count
    for i in range(len(array)):
        idx = array[i]
        count_array[idx] += 1

    # 최대값 검색
    max_idx = 0
    for i in range(len(count_array)):
        if count_array[i] > count_array[max_idx]:
            max_idx = i

    # 중복값 검색
    dup_count = 0
    for i in range(len(count_array)):
        if count_array[i] == count_array[max_idx]:
            dup_count += 1
    
    if dup_count > 1:
        answer = -1
    else:
        answer = max_idx

    return answer
