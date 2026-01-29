def subset(arr,target,n,dp):
    if n==0:
        return False
    if target==0:
        return True
    if dp[n][target]=-1:
         return dp[n][target]
    if arr[n-1]>target:
        dp[n][target]=subset(arr,n-1,target,dp)
    else:
        include=subset(arr,n-1,target-arr[n-1],dp)
        exclude=subset(arr,n-1,target,dp)
        dp[n][target]=include or exclude
        return dp[n][target]
    # if arr(n-1)>sum:
    #     return subset(arr,sum,n-1)
    # else:
    #     return subset(arr,sum-arr[n-1],n-1) or subset(arr,sum,n-1)
arr=[2,3,7,8,10]
target=11
n=len(arr)
dp=[[-1 for _ in range(target+1)for_ in range(n+1)]]
result=subset(arr,target,n,dp)
print(result)