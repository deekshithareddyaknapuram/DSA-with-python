
def knapsack_memo(weight,profit,W,n,memo):
    if W==0 or n==0:
        return 0
    if (n,W)in memo:
    # if wt[n-1]>w:
        memo[(n,W)]=knapsack_memo(weight,profit,W,n-1,memo)
    else:

        # return knapsack(wt,prof,w,n-1)
     include=(profit[n-1]+knapsack_memo(weight,profit,W-weight[n-1],n-1,memo))
     exclude=knapsack_memo(weight,profit,W,n-1,memo)
weight=[4,5,1]
profit=[1,2,3]
n1=len(profit)
memo={}

# W=8
# n=4
print(knapsack_memo(weight,profit,W,n1,memo))