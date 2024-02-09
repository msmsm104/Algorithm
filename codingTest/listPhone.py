# listPhone.py

# 입력값 - 전화번호 목록

# 출력값 - boolean

phone_book = ["12","123","1235","567","88"]

def solution(phone_book):
    # 정렬
    phone_book.sort()
    
    # 순차 탐색
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    
    return True

print(solution(phone_book))

            

# result = ""

# # 순차 탐색
# for i in range(len(phone_book)):
#     for j in range(i + 1, len(phone_book)):
#         if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#             result += "False"
#         else:
#             result += "True"



# print(result)
        