if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxval = max(arr)
    for i in sorted(arr):
        if(i < maxval):
            val = i
            
    print(val)
