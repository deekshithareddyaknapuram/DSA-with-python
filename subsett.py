#recurcive 
'''def difference(arr,n,sum_calculated,sum_total):
    if n==0:
        return abs((sum_total-sum_calculated)-sum_calculated)
    include=difference(arr,n-1,sum_calculated+arr[n-1],sum_total)
    exclude=difference(arr,n-1,sum_calculated,sum_total)
    return min(include,exclude)
def min_difference(arr):
    sum_total=0
    for num in arr:
        sum_total+=num
    return min_difference(arr,len(arr),0,sum_total)
arr=[1,6,5,11]
print(min_difference(arr))'''
#memoization
'''def difference(arr,n,sum_calculated,sum_total,memo):
    if n==0:
        return abs((sum_total-sum_calculated)-sum_calculated)
    if(n,sum_calculated) in memo:
        return memo[(n,sum_calculated)]
    include=difference(arr,n-1,sum_calculated+arr[n-1],sum_total)
    exclude=difference(arr,n-1,sum_calculated,sum_total)
    memo[(n,sum_calculated)]=min(include,exclude)
    return memo[(n,sum_calculated)]
def min_difference(arr):
    sum_total=sum(arr)
    memo={}
    return min_difference(arr,len(arr),0,sum_total)
arr=[1,6,5,11]
print(min_difference(arr))'''
# tabulation
def min_difference(arr):
    total_sum=sum(arr)
    n=len(arr)
    half_sum=total_sum//2
    dp=[[False]*(half_sum+1)for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,half_sum+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i - 1][j] + dp[i - 1][j-arr[i - 1]]
            else:
                dp[i][j]=dp[i - 1][j]
    for j in range(half_sum,-1,-1):
        if dp[n][j]:
            return total_sum-2*j

arr=[1,6,5,11]
print(min_difference(arr))