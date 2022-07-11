#!/bin/python3

import os

def timeConversion(s):
    if('PM' in s and s[:2] != '12'): 
        s = f'{int(s[:2]) + 12}{s[2:]}'
    elif('AM' in s and s[:2] == '12'):
            s = f'00{s[2:]}'     
    return(s[:8])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()