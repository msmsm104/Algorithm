# code_1-1.py
# 팩토리얼 구현

# 점화식을 통한 재귀함수 구현
# n! = (n-1)! x n

# 함수 구현
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

if __name__=="__main__":
    # 입력값 (숫자_정수)
    input_number = int(input("숫자를 입력해 주세요 : "))
    print(f"입력값 : {input_number}")

    # 출력값 (팩토리얼 수식)
    print(f"{input_number}! = {factorial(input_number)}")