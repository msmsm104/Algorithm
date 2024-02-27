#!/bin/python3

import math
import os
import random
import re
import sys

def stairCase(n):

    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * i)

if __name__=="__main__":
    n = int(input().strip())

    stairCase(n)