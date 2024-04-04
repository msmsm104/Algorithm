# operation_count.py
# 함수의 연산 횟수 

                        # 연산  빈도수
def func(arr, init):    
    n = len(arr)        #  1     1
    ret = init          #  1     1
    for i in range(n):  #  1     n
        ret += arr[i]   #  1     n
    return ret          #  1     1
                        #       2n + 3


if __name__=="__main__":
    arr = [1, 2, 3, 4, 5]
    result = func(arr, 10)
    print(result)