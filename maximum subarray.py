arr=list(map(int,input().split()))
n=len(arr)
maxi=arr[0]
sum=arr[0]
for i in range(1,n):
    sum=max(arr[i],sum+arr[i])
    maxi=max(maxi,sum)
print(maxi)
