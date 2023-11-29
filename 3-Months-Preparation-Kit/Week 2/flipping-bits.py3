#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    bit31 = str(bin(n))[2:]
    flip = ""
    for i, v in enumerate(bit31):
        if v == '0':
            flip += v.replace(v, '1', 1)
        else:
            flip += v.replace(v, '0', 1)
    length = 32 - len(flip)
    ones = '1'*length
    flip = ones + flip
    
    return int(flip, 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
