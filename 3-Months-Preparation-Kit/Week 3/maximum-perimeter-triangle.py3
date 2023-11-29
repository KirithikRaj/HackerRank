#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#
def subset(a, size):
    t = []
    if size == 0:
        yield t
    elif size == 1:
        for i in range(len(a)):
            t = [a[i]]
            yield t
    else:
        for i in range(len(a)-size+1):
            for item in subset(a[i+1:], size-1):
                t = [a[i]]
                for x in item:
                    t.append(x)
                yield t

def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks.sort()
    sets = []
    for item in subset(sticks, 3):
        sets.append(item)
    triangles = []
    for item in sets:
        a, b, c = item
        if item not in triangles and a+b>c and a+c>b and b+c>a:
            triangles.append(item)
    perimeters = []*len(triangles)
    for item in triangles:
        perimeters.append(sum(item))
    if perimeters:
        maximum = max(perimeters)
        counts = perimeters.count(maximum)
        if counts == 1:
            ind = perimeters.index(maximum)
            return (triangles[ind])
        else:
            for item in perimeters:
                if item != maximum:
                    triangles.remove(item)
            max_of_sides = []
            min_of_sides = []
            for item in triangles:
                max_of_sides.append(max(item))
                min_of_sides.append(min(item))
            count_max = max_of_sides.count(max(max_of_sides))
            count_min = min_of_sides.count(max(min_of_sides))
            if count_max == 1:
                return triangles[max_of_sides.index(max(max_of_sides))]
            elif count_min == 1:
                return triangles[min_of_sides.index(max(min_of_sides))]
            else:
                ind = []
                for item in min_of_sides:
                    if item == max(min_of_sides):
                        ind.append(min_of_sides.index(item))
                return triangles[ind[0]]
    else:
        return [-1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
