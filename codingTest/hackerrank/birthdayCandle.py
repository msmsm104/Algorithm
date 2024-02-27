# birthdayCandle.py

import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):

    max_idx = 0
    result = 0
    for i in range(len(candles)):
        if candles[i] > candles[max_idx]:
            max_idx = i
    for x in candles:
        if x == candles[max_idx]:
            result += 1
    
    return result


if __name__ == "__main__":
    n = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    birthdayCakeCandles(candles)