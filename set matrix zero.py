# arr=list(map(int,input().split()))

n=int(input())
m=int(input())
arr=[list(map(int,input().split()))
for _ in range(n)]
col0=1
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            arr[i][0]=0
            if j!=0:
                arr[0][j]=0
            else:
                col0=0
for i in range(1,n):
    for j in range(1,m):
            if arr[i][0]==0 or arr[0][j]==0:
                arr[i][j]=0
if arr[0][0]==0:
    for j in range(m):
        arr[0][j]=0
if col0==0:
    for i in range(n):
        arr[i][0]=0
print(arr)
