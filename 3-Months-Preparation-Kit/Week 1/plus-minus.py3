#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    t = len(arr)
    p, n, zero = 0, 0, 0
    for x in arr:
        if x > 0:
            p += 1
        elif x < 0:
            n += 1
        else:
            zero += 1
    print(str.format('{0:.6f}', p/t))
    print(str.format('{0:.6f}', n/t))
    print(str.format('{0:.6f}', zero/t))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
