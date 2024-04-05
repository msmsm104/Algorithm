# sampleModule.py

class DynamicArray:
    def __init__(self, arr):       # 생성자
        self.arr = arr             # 객체변수 arr 생성

    def len(self):                  # len 메서드
        result = len(self.arr)
        return result
    
    def append(self, elem):
        self.arr = self.arr + [elem]
        return None

    def pop(self):
        self.arr, result = self.arr[:-1], self.arr[-1]
        return result
        



if __name__=="__main__":
    a = DynamicArray([1,2,3,4])

    print(a.arr)
    
    a.append(5)
    print(a.arr)

    print(a.pop())
    print(a.pop())
    print(a.arr)