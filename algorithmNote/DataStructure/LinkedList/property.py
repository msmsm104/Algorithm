# property.py

class MyClass:
    def __init__(self):
        self.__data = None

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if value < 0:
            raise ValueError("음수는 허용되지 않습니다.")
        self.__data = value

if __name__=="__main__":
    obj = MyClass()

    print(obj.data)

    obj.data = 100

    print(obj.data)

    obj.data = -10

    print(obj.data)

