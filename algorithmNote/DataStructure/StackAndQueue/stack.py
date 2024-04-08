# stack.py

class Stack:
    def __init__(self):
        self.container = list() # 내부 표현: 실제로 데이터를 담을 객체는 동적 배열

    def empty(self):
        if not self.container:
            return True
        else:
            return False
        
    def push(self, data):
        self.container.append(data)
    
    def pop(self):
        if self.empty():
            return None
        return self.container.pop()
    
    def peek(self):
        if self.empty():
            return None
        return self.container[-1]
        

if __name__=="__main__":
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    while not s.empty():
        print(s.pop(), end=" ")
        