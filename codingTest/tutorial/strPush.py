# strPush.py
# 문자열 밀기 문제

# 입력값 A, B
A, B = "abc", "bca"

def strPush(A, B):
    # 출력값
    answer = 0
    # 될수 있는지 없는지 확인
    YN = False
    right_count = 0
    while right_count < len(A):
        # 오른쪽으로 밀기
        print(A, right_count)
        if A == B:
            YN = True
            break
        else:
            A = A[len(A) - 1] + A[:len(A) - 1]
            right_count += 1
    if YN:
        print(len(A) - right_count, right_count)
        answer = right_count
    else:
        answer = -1
    return answer

    # # 왼쪽으로 밀기
    # left_count = 0
    # for _ in range(len(A)):
    #     print(A, left_count)
    #     if A == B:
    #         break
    #     else:
    #         A = A[1:] + A[0]
    #         left_count += 1

    



# 가능 여부에 따라서 다른 결과값 출력
# if YN:

# else:
#     answer = -1


print(strPush(A,B))