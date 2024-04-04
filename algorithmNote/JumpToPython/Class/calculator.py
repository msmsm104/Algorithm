# calculator.py
# 사칙연산 클래스 생성

class FourCal:
    def __init__(self, first, second): # 생성자를 통해 초기값 설정
        self.first = first
        self.second = second
    # def setdata(self, first, second):
    #     self.first = first      # 객체 self의 객체변수 first 생성
    #     self.second = second    # 객체 self의 객체변수 second 생성
    
    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
    
class MoreFourCal(FourCal):     # FourCal 클래스를 상속
    def pow(self):
        result = self.first ** self.second
        return result
    

class SafeFourCal(FourCal):     # FourCal 클래스를 상속
    def div(self):
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
            return result

if __name__=="__main__":
    a = SafeFourCal(4, 0)

    print(a.add())
    print(a.sub())
    print(a.mul())
    print(a.div())