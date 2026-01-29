def SumOfk(arr,k):
    arr=list(map(int,input().split()))
    k=int(input())

    sum=0

    for i in arr:
        sum+=i
        k=sum-arr[i]
    return k
arr=list(map(int,input().split()))
k=int(input())
print(SumOfk(arr,k))