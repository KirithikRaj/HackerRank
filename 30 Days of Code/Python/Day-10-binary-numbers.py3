#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    binary = ""
    while n!=1:
        binary += str(n % 2)
        n = n//2
    binary += '1'
    binary = "".join(reversed(binary))
    max_ones = 0
    ones = 0
    for i, v in enumerate(binary):
        if v == '1':
            ones += 1
        elif v == '0' or ones>=max_ones:
            if ones>= max_ones:
                max_ones = ones
            ones = 0
    if max_ones == 0 or ones>max_ones:
        max_ones = ones
    print(max_ones)
