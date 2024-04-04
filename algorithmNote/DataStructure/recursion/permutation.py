# permutation.py
# 순열을 재귀함수로 구현

def permutation(arr, start):

    # base case(기저 조건)
    if len(arr) - 1 == start:
        print(arr)
        return
    
    for idx in range(start, len(arr)):
        arr[start], arr[idx] = arr[idx], arr[start]
        permutation(arr, start + 1)
        arr[start], arr[idx] = arr[idx], arr[start]



if __name__=="__main__":
    arr = [1, 2, 3]
    permutation(arr, 0)