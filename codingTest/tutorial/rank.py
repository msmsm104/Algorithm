# rank.py
# 등수 매기기

# 입력값
score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]

# 출력값 예시 - result - [4, 4, 6, 2, 2, 1, 7]

def rank(score):
    # 영어, 수학 점수 평균
    avg_array = [(sum(x) / len(x)) for x in score]
    
    result = []
    # 각각 점수보다 작은값이 몇명이나 존재하는지
    for i in range(len(avg_array)):
        count = 0
        for j in range(len(avg_array)):
            if avg_array[i] < avg_array[j]:
                count += 1
        result.append(count + 1)

    return result

print(rank(score))