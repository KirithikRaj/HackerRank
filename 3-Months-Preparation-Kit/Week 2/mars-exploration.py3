#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    n = int(len(s)/3)
    r = len(s) % 3
    arr = "SOS"*n
    if r == 1:
        arr += 'S'
    else:
        arr += 'SO'
    c = 0
    for i, v in enumerate(s):
        if s[i] != arr[i]:
            c += 1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
