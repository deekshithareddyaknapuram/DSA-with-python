def CountOfSub(i,arr,curr_sum,k):
    if i==len(arr):
        return 1 if curr_sum==k else 0
            
    pick=CountOfSub(i+1,arr,curr_sum+arr[i],k)
    not_pick=CountOfSub(i+1,arr,curr_sum,k)
    return pick+not_pick
arr=list(map(int,input().split()))
k=int(input())
print(CountOfSub(0,arr,0,k))