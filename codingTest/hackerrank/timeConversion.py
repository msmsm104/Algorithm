# timeConversion.py

import math
import os
import random
import re
import sys


def timeConversion(time):

    hour = int(time[:2])
    t_zone = time[-2:]

    if t_zone == "AM" and hour >= 12:
        hour -= 12
    elif t_zone == "PM" and hour < 12:
        hour += 12

    if len(str(hour)) == 1:
        result = "0" + str(hour) + time[2:-2]
    else:
        result = str(hour) + time[2:-2]
    
    return result


if __name__ == "__main__":
    # 입력값
    s = input().strip()
    
    timeConversion(s)