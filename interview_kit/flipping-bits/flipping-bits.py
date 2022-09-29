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

def convert_decimal_to_binary(num):
    bin_num = ""
    dividend = num
    if num == 0:
        bin_num = '0'
        return bin_num
    while dividend != 0:
        rem = int(dividend % 2)
        dividend = int(dividend / 2)
        bin_num = bin_num + str(rem)
    bin_num = bin_num[::-1]
    return bin_num
    
def flip(bin_num):
    flip_bi_num = ''
    for x in bin_num:
        if x == '1':
            flip_bi_num = flip_bi_num + '0'
        else:
            flip_bi_num = flip_bi_num + '1'
    return flip_bi_num
    

def convert_binary_to_decimal(num):
    i = len(num)-1
    result = 0
    for x in num:
        if x == '1':
            power_res = math.pow(2, i)
            result = result + power_res
        i = i - 1
    return result
    
    
def flippingBits(n):
    # Write your code here
    bin_num = convert_decimal_to_binary(n)
    bin_num = bin_num.zfill(32)
    flip_bi_num = flip(bin_num) 
    result = convert_binary_to_decimal(flip_bi_num)
    return str(int(result))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
