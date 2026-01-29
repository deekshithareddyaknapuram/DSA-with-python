'''def CountConversion(arr):
    n=len(arr)
    c=0
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                c+=1
    return c
arr=list(map(int,input().split()))
print(CountConversion(arr))'''
def ReversePair(arr):
    # arr.sort()
    n=len(arr)
    c=0
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]>2*arr[j]:
                c+=1
    return c
arr=list(map(int,input().split()))
print(ReversePair(arr))
