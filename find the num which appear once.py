def appearonce(arr):
    nums=0
    for i in range(0,len(arr)):
        nums^=arr[i]
    return nums
arr=list(map(int,input().split( )))
print(appearonce(arr))