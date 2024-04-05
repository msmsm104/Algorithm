# mod2.py
# 변수, 클래스, 함수를 포함하는 모듈

PI = 3.141592


class Math:
    def solv(self, r):
        result = PI * (r ** 2)
        return result
    

def add(a, b):
    result = a + b
    return result

if __name__=="__main__":
    print(f"PI : {PI}")
    print(f"add(4, 2) : {add(4, 2)}")

    a = Math()
    print(f"a.solv(5) : {a.solv(5)}")