def ece(arr,d,n):
    MOD=10**9+7
    total=sum(arr)
    if (total+d)%2!=0:
        return 0
    target=(total+d)//2
    dp=[0]*(target+1)
    dp[0]=1
    for num in arr:
        for j in range(target,num-1,-1):
            dp[j]=(dp[j]+dp[j-num])%MOD
    return dp[target]
arr=[1,1,1,1,1]
n=5
d=3
print(ece(arr,d,n))