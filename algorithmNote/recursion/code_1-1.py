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
    
# 입력 유효성 검사
def get_valid_input():
    while True:
        try:
            input_number = int(input("숫자를 입력해 주세요: "))
            if input_number < 0:
                print("음수는 입력할 수 없습니다. 다시 입력해 주세요.")
            else:
                return input_number
        except ValueError:
            print("잘못된 입력입니다. 정수를 입력해 주세요.")

if __name__=="__main__":
    # 반복 입력 지원
    while True:
        # 입력값 (숫자_정수)
        input_number = get_valid_input()
        # 출력값 (팩토리얼 수식)
        print(f"{input_number}! = {factorial(input_number)}")
        continue_or_quit = input("계속하려면 'y', 종료하려면 다른 키를 누르세요: ")
        if continue_or_quit != "y":
            break
        