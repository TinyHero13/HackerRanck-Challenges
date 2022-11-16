#!/bin/python3
import math
import os
import random
import re
import sys

def twoArrays(n, k, A, B):
    A, B = sorted(A), sorted(B, reverse=True)
    result = ' '
    for i in range(0, n-1):
        if(A[i] + B[i] < k):
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        A = list(map(int, input().rstrip().split()))
        B = list(map(int, input().rstrip().split()))
        result = twoArrays(n, k, A, B)
        fptr.write(result + '\n')
    fptr.close()
