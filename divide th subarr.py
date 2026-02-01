def DivideTheSubarr(arr):
    # n=len(arr)
    # sum=0
    mini=arr[0]
    rest=arr[1:]
    rest.sort()
    
    return mini+rest[0]+rest[1]
num=list(map(int,input().split()))
print(DivideTheSubarr(num))

                