# node.py

class Node:
    def __init__(self, data = None):
        self.__data = data
        self.__prev = None
        self.__next = None

    # 소멸자 : 객체가 사라지기 전 반드시 호출
    # 삭제 연산 때 삭제되는 것을 확인하고자 작성
    def __del__(self):
        print(f"data of {self.data} is deleted")

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, p):
        self.__prev = p

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, n):
        self.__next = n