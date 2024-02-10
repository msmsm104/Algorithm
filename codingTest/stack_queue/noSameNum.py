# noSameNum.py

from collections import deque

arr = [1,1,3,3,0,1,1]

result = [None]

# 1. 순차적으로 append 하는데 이전에 넣었던 값이랑 동일한 경우 append 하지 않음
for num in arr:
    if result[-1] != num:
        result.append(num)

print(result)



