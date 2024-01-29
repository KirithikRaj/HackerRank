#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        sets = (arr[i:i+3]) #Subset of three rows
        #print('set', sets)
        for j in range(4):
            sub = [] #sub matrix of 3 columns
            sub.append(sets[0][j:j+3])
            sub.append(sets[1][j:j+3])
            sub.append(sets[2][j:j+3])
            sub[1][0] = 0
            sub[1][2] = 0
            #print('sub, j: ', j, sub)
            tot = 0
            for row in sub:
                for el in row:
                    tot += el
            if i == 0 and j == 0: #assign initial value of max_sum from 1rst total
                max_sum = tot
            elif tot>max_sum:
                max_sum = tot
            #print(tot, max_sum)
    print(max_sum)
