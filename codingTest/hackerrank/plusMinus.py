# /bin/python3
import math
import os
import random
import re
import sys

def plusMinus(arr):
    
    pos_cnt = 0
    neg_cnt = 0
    zero_cnt = 0
    length_arr = len(arr)
    for i in range(len(arr)):
        if arr[i] > 0:
            pos_cnt += 1
        elif arr[i] < 0:
            neg_cnt += 1
        else:
            zero_cnt += 1
    
    result_arr = [pos_cnt, neg_cnt, zero_cnt]
    for x in result_arr:
        print(f"{x / length_arr:.6f}")

if __name__=="__main__":
    n = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)



