
n=int(input())
arr=[]
for _ in range(n):
    s,e=map(int,input().split())
    arr.append([s,e])
arr.sort()
ans=[]
for i in range(0,n):
    if not ans or arr[i][0]>ans[-1][1]:
        ans.append(arr[i])
    else:
        ans[-1][1]=max(ans[-1][1],arr[i][1])
print(ans)
