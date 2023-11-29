#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    month = [31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < 1918:
        if year % 4 == 0:
            month.insert(1,29)
        else:
            month.insert(1, 28)        
    elif year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            month.insert(1, 29)
        else:
            month.insert(1, 28)
            print('no')
    else:
        month.insert(1, 15)
    m, i = 0, 0
    while m < 256:
        m += month[i]
        i += 1
    d = 256 - (m - month[i - 1])
    m = i
    if d<10:
        d = '0' + str(d)
    if m<10:
        m = '0' + str(m)
    return (str(d)+'.'+str(m)+'.'+str(year))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
