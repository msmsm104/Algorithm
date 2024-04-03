# code_1-1.py
# 팩토리얼 구현

# 점화식을 통한 재귀함수 구현
# n! = (n-1)! x n
class FactorialCalculator:
    def __init__(self):
        self.factorial_cache = {}

    def factorial(self, n):
        if n < 0:
            raise ValueError("음수의 팩토리얼은 정의되지 않습니다.")
        elif n == 0:
            return 1
        elif n in self.factorial_cache:
            return self.factorial_cache[n]
        else:
            result = self.factorial(n-1) * n
            self.factorial_cache[n] = result
            return result
        
    
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
    calculator = FactorialCalculator()
    while True:
        # 입력값 (숫자_정수)
        input_number = get_valid_input()
        result = calculator.factorial(input_number)
        # 출력값 (팩토리얼 수식)
        print(f"{input_number}! = {result}")
        continue_or_quit = input("계속하려면 'y', 종료하려면 다른 키를 누르세요: ")
        if continue_or_quit.lower() != "y":
            break