# calculator.py
# 사칙연산 클래스 생성

class FourCal:
    def setdata(self, first, second):
        self.first = first      # 객체 self의 객체변수 first 생성
        self.second = second    # 객체 self의 객체변수 second 생성
    
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
    
if __name__=="__main__":
    a = FourCal() # 객체 a 생성, a는 FourCal 클래스의 인스턴스
    b = FourCal()
    a.setdata(4, 2)
    b.setdata(3, 8)

    print("객체 a에 대한 사친연산")
    print(a.add())
    print(a.sub())
    print(a.mul())
    print(a.div())
    print("")
    print("객체 b에 대한 사친연산")
    print(b.add())
    print(b.sub())
    print(b.mul())
    print(b.div())
