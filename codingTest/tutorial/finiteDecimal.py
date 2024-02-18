# finiteDecimal.py
# 유한소수 판별하기

# 입력값
a, b = 12, 21


# 함수로 정의 
def solution(a, b):
    # 출력값
    answer = 0

    # 입력값의 기약분수 표현
    # 분자, 분모값을 각각 소인수 분해해서 list형태로 표현
    all_array = []
    a_array = []
    b_array = []

    # 0 <= a, b <= 1000 범위의 모든 소인수 값
    for i in range(1, 1000 + 1):
        count = 0
        for j in range(1 ,i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            all_array.append(i)


    # a에 대해 소인수 분해
    for i in all_array:
        while a % i == 0:
            a = a // i
            a_array.append(i)
        if i > a:
            break
    for i in all_array:
        while b % i == 0:
            b = b // i
            b_array.append(i)
        if i > b:
            break

    print(a_array)
    print(b_array)

    # 기약분수로 만들기 - 중복되는 값이 존재하면 양쪽에서 제거
    for i in range(len(a_array)):
        for j in range(len(b_array)):
            if a_array[i] == b_array[j]:
                a_array[i], b_array[j] = -1, -1
                # del a_array[i]
                # del b_array[j]
                break
    print(a_array)
    print(b_array)

    result = set(list(filter(lambda x: x != -1, b_array)))

    # 분모 - b_array의 set 값에 2, 5만 포함
    print({2, 5} == result or {2} == result or {5} == result)


## 테스트 케이스에서 오답이 발생하는 경우가 나옴
    
    