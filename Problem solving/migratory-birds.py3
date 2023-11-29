#!/bin/parrthon3

import math
import os
import random
import re
import sys
#
# Complete the 'migratorarrBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAarr arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    arr.sort()
    distinct = []
    for x in arr:
        if x not in distinct:
            distinct.append(x)
    i = 0
    counts = [0]*len(distinct)
    for i in range(len(distinct)):
        j = 0
        while j < len(arr):
            if distinct[i] == arr[j]:
                counts[i] += 1
            j += 1
    for i in range(len(counts)):
        if counts[i] == max(counts):
            mode_index = i
            break
    return distinct[mode_index]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
