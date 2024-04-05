# principleOfLocality.py
# 지역성의 원리

def sum_all(arr):       # 연산      # 빈도
    ret = 0             #  1          1
    for elem in arr:    #  1          n
        ret += elem     #  1          n
    return ret          #  1          1
                        #  T(n) = 2n + 2
