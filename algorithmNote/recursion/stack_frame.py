# stack_frame.py
# 함수가 호출되면 메모리에서는 스택 프레임이라는 공간이 생깁니다.
# 이 스택 프레임에는 함수 실행에 필요한 지역 변수들이 할당됩니다.

def add_two(a, b):
    c = a + b
    return c


if __name__=="__main__":
    # 프로그램이 끝날때까지 메모리에 유지되는 전역 변수
    a = 10
    b = 20

    # 스택 프레임 생성
    # 함수 내부에 있는 매개변수 a, b/ 그 결과값을 담을 지역 변수 c가 저장
    result = add_two(a, b)

    print(result)