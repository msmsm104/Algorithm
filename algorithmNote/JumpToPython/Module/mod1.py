# mod1.py
# 샘플 모듈
# 모듈 - 함수, 변수 또는 클래스를 모아놓은 파일

def add(a, b):
    result = a + b
    return result

def sub(a, b):
    result = a - b
    return result


if __name__=="__main__":
    print(add(1, 4))
    print(sub(4, 2))