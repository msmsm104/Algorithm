# dynamicArrayTest.py

from dynamicArray.sampleModule import DynamicArray

dArray = DynamicArray([1,2,3,4])

print(dArray.arr) # 객체 변수

# 메서드 테스트 (수정사항)

dArray.append([1,2,3,4])
print(dArray.arr)

dArray.pop()
print(dArray.arr)
