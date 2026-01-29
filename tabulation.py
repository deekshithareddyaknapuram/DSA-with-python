# Bottom-Up dp(Tabulation):
def knapsack_tabulation(wt,prof,w,n):
    dp=[[0 for _ in range(w+1)]for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,w+1):
            if wt[i-1]<=w:
                dp[i][w]=max(prof[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
        return dp[n][w]
wt=[2,3,4,1]
prof=[1,8,2,3]
w=8
n=4
print(knapsack_tabulation(wt,prof,w,n))


