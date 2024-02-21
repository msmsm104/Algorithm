# fractionalSum.py
# 분수의 덧셈

# 입력값
numer1, denom1, numer2, denom2 = 9, 2, 1, 3

# 출력값
result = []

# 알고리즘
# 분모값들(denom1, denom2)의 최소공배수
# 각 분모를 인수분해 한 값
# 서로소 자료형 (리스트)
array = []
for i in range(1, 1000):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        array.append(i)

# 인수분해 함수 정의
def inSu(num):
    elem_denom = []
    for i in range(len(array)):
        while num % array[i] == 0:
            num = num // array[i]
            elem_denom.append(array[i])
            if num == 1:
                break
    return elem_denom

# 각 분모에 대해 인수분해
denom1_lst = inSu(denom1)
denom2_lst = inSu(denom2)

print(denom1_lst, denom2_lst)
sum_denom = []
for value in list(set(denom1_lst + denom2_lst)):
    i = max(denom1_lst.count(value), denom2_lst.count(value))
    for j in range(i):
        sum_denom.append(value)
print(sum_denom)

for value in list(set(denom1_lst + denom2_lst)):
    i = denom2_lst.count(value) - denom1_lst.count(value)
    if i == 0:
        print(f"pass value: {value}")
        pass
        
    elif i > 0:
        numer1 *= value ** abs(i)
        print(f"number1 * {value} {i}")
    elif i < 0:
        numer2 *= value ** abs(i)
        print(f"number2 * {value} {i}")

print(numer1 + numer2)
total_denom = 1
for i in sum_denom:
    total_denom *= i
print(total_denom)

print(inSu(numer1 + numer2))
print(inSu(total_denom))


