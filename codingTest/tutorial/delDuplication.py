# delDuplication.py
# 중복 문자 제거

my_string = input()

# print(set(list(my_string)))

def delDuplication(data):
    answer = ""

    for x in data:
        if x not in answer:
            answer += x

    return answer

print(delDuplication(my_string))