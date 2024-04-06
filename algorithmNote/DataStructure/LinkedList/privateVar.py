# privateVar.py (Encapsulation)
# 데이터를 외부에서 직접적으로 접근하지 못하도록 보호, 메서드를 통해 데이터를 조작

class BankAccount:
    def __init__(self, balance = 0):
        self.__balance = balance # private 변수로 지정

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("잔액이 부족합니다.")

    def get_balance(self):
        return self.__balance

if __name__=="__main__":
    a = BankAccount()

    a.deposit(100)
    a.withdraw(110)
    print(a.get_balance())

    