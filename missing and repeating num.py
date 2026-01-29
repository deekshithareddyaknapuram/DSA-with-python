arr=list(map(int,input().split()))
n=int(input())
s=0
s2=0
for i in arr:
    s+=i
    s2+=i*i
ns=n*(n+1)//2
ns2=n*(n+1)*(2*n+1)//6
# m=len(arr)

val1=s-ns
val2=s2-ns2
val2=val2//val1
x=(val1+val2)//2
y=x-val1
print(x,y)
