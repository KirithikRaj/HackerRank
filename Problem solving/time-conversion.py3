#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = s[:-2]
    if s[-2:] == "AM":
        if s[:2] == str(12):
            time = '00' + time[2:]
    else:
        if s[:2] != str(12):
            time = str(int(time[:2]) + 12) + time[2:]
    return time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
