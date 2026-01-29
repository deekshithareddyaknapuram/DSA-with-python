'''def cutrodrecur(i,prices):
    if i==0:
        return 0
    ans=0
    for j in range(1,i+1):
        ans=max(ans,prices[j-1]+cutrodrecur(1-j,prices))
    return ans
def cutrod(prices):
    n=len(prices)
    return cutrodrecur(n,price)
prices=[1,5,8,9,10,17,17,20]
print(cutrod(prices))'''
#memoization
def cutrodrecur(i,prices,memo):
    if i==0:
        return 0
    if memo[i-1]!=-1:
         return[i-1]
    ans=0
    for j in range(1,i+1):
        ans=max(ans,prices[j-1]+cutrodrecur(1-j,prices,memo))
        memo[i-1]=ans
    return ans
def cutrod(prices):
    n=len(prices)
    memo=[-1]*n
    return cutrodrecur(n,prices,memo)
prices=[1,5,8,9,10,17,17,20]
print(cutrod(prices))
#tab
'''def cutrodrecur(i,prices,memo):
    if i==0:
        return 0
    if memo[i-1]!=-1:
         return[i-1]
    ans=0
    for j in range(1,i+1):
        ans=max(ans,prices[j-1]+cutrodrecur(1-j,prices,memo))
        memo[i-1]=ans
    return ans
def cutrod(prices):
    n=len(prices)
    memo=[-1]*n
    return cutrodrecur(n,prices,memo)
prices=[1,5,8,9,10,17,17,20]
print(cutrod(prices))
'''