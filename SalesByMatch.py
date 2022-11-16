#!/bin/python3
import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    lst, count = [], 0
    for i in set(ar):
        lst.append(ar.count(i))
        
    for j in lst:
        if(j >= 2):
            count += j // 2  
                
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
