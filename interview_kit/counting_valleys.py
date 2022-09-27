#!/bin/python3

import math
import os
import random
import re
import sys


def countingValleys(steps, path): 
    valley = 0
    down = 0
    for unit in path:
        if unit == 'D':
            down += 1
        else:
            down -= 1
            if down == 0:
                valley += 1
    return valley
                
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
