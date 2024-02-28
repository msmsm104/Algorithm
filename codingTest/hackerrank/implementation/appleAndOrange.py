# appleAndOrange.py

import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):

    for i in range(len(apples)):
        apples[i] += a
    
    for i in range(len(oranges)):
        oranges[i] += b

    apples_count = 0
    oranges_count = 0
    for i in range(len(apples)):
        if apples[i] >= s and apples[i] <= t:
            apples_count += 1
    
    for i in range(len(oranges)):
        if oranges[i] >= s and oranges[i] <= t:
            oranges_count += 1

    print(apples_count)
    print(oranges_count)


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

