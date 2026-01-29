def subset(arr,sum,n):
    if n==0:
        return False
    if sum==0:
        return True
    if arr[n-1]>sum:
        return subset(arr,sum,n-1)
    else:
        return subset(arr,sum-arr[n-1],n-1) + subset(arr,sum,n-1)
arr=[2,3,7,8,10]
sum=9
result=subset(arr,sum,len(arr))
print(result)