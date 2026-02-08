def Sumofk(i,arr,temp,curr_sum,k):
    if i==len(arr):
        if curr_sum==k:
            print(temp)
        return
    Sumofk(i+1,arr,temp+[arr[i]],curr_sum+arr[i],k)
    Sumofk(i+1,arr,temp,curr_sum,k)
arr=list(map(int,input().split()))
k=int(input())
Sumofk(0,arr,[],0,k)