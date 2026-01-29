def LCN(arr):
    if not arr:
        return 0
    arr=sorted
    longest=1
    stack=[]
    for i in stack:
        if stack[i]<stack[i+1]:
            longest=1
        else:
            longest+=1
            longest=max(longest,stack)
arr=list(map(int,input().split()))
print(arr)
'''if not arr: 
    
  print (0)
arr=sorted(arr)

longest=1
curr=1
# prev=curr-1
for i in range(1,len(arr)):
  if arr[i]==arr[i-1]+1:
    curr+=1
  elif arr[i]!=arr[i-1]:
    curr=1
  longest=max(longest,curr)
print(arr,longest)
'''