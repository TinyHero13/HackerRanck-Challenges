def plusMinus(arr):
    countP, countN, countZ = 0, 0, 0
    
    for i in arr:
        if(i > 0):
            countP += 1
        elif(i < 0):
            countN += 1
        else:
            countZ += 1

    print(f'{countP/len(arr):.6f}\n{countN/len(arr):.6f}\n{countZ/len(arr):.6f}')
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)