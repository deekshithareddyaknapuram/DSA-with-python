# arr= 1 2 1  3 2
# olp=2 how many number appeared more than once
'''def numberappeared(arr,num):
    if not  arr:
        return 0

    n=len(arr)
    c=0
    for i in range(0,n):
        if arr[i]==num:
            c+=1
    return c
arr=list(map(int,input().split()))
num=int(input())
print(numberappeared(arr,num))
'''
# using hashing
def numappeared(arr):
   
    hash={}
    for n in arr:
        if n in hash:
           
          hash[n]+=1
        else:
           hash[n]=1
    return hash
arr=list(map(int,input().split()))
print(numappeared(arr))

        
