#!/bin/python3

import os

def breakingRecords(scores):
    countmin, countmax = 0, 0
    max, min = scores[0], scores[0]
    for i in scores:
        if(i > max):
            max = i
            countmax += 1
        elif(i < min):
            min = i
            countmin += 1
            
    return(countmax, countmin)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()