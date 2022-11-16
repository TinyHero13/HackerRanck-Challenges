#!/bin/python3
def miniMaxSum(arr):
    arr = sorted(arr)
    print(sum(arr[:-1]), sum(arr[1:]))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
