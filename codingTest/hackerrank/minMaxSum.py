#! algorithm_env/bin/python3

import math
import os
import random
import re
import sys


def minMaxSum(arr):

    total_sum = sum(arr)
    min_idx = 0
    max_idx = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
        if arr[i] > arr[max_idx]:
            max_idx = i
    
    print(total_sum - arr[max_idx], total_sum - arr[min_idx])


if __name__=="__main__":
    arr = list(map(int, input().rstrip().split()))

    minMaxSum(arr)
    