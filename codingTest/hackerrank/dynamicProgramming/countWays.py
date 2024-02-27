# countWays.py

import math
import os
import random
import re
import sys

def count_ways(weights, l, r):
    # dp 배열 초기화
    dp = [0] * (r + 1)
    dp[0] = 1

    for weight in weights:
        # dp[i] => i가 되기위한 경우의 수 (weight를 제외했을때)
        # dp[i - weight] => i가 되기위한 경우의 수 (weight를 포함했을때)
        for i in range(weight, r + 1):
            dp[i] += dp[i - weight]
        # print(f"weight: {weight}")
        # print(dp)
        # print("")
    dp = dp[l:]
    print(dp)
    return sum(dp)



if __name__ == "__main__":
    weights = [1, 2, 3]
    l = 1
    r = 6

    print(count_ways(weights, l, r))

