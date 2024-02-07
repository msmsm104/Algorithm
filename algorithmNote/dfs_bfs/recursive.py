# recursive.py
# 재귀 함수의 종료 조건 명시

def recursive_function(i):
    if i == 100:
        return
    print(f"{i}번째 재귀함수에서 {i + 1}번째 재귀함수를 호출합니다.")
    recursive_function(i + 1)
    print(f"{i}번째 재귀 함수를 종료합니다.")

recursive_function(1)