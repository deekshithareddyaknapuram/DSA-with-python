'''def subarr(arr,k):
    n=len(arr)
    # sum=0
    count=0
    for i in range(0,n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            # count+=1
            if sum==k:
                count+=1

    #     sum+=i
    #     k=sum-arr[i]
    return count
arr=list(map(int,input().split()))
k=int(input())
print(subarr(arr,k))
'''
def subarr(arr,k):
    # n=len(arr)
    presum=0
    count=0
    hash={0:1}
    for num in arr:
        presum+=num
        if presum-k in hash:
            count+=hash[presum-k]
            
        hash[presum]=hash.get(presum,0)+1
    return count
arr=list(map(int,input().split()))
k=int(input())
print(subarr(arr,k))


