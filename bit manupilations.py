'''#MinBitflip to covert a number
def MinBitFlip(start,target):
    ans=start^target
    c=0
    while ans>0:
        ans= ans &( ans-1)
        c+=1
    return c
start=int(input(),2)
target=int(input(),2)
print(MinBitFlip(start,target))
#count the number of set bits
def SetBits(num):
    c=0
    
    while num>0:
        c+=num&1
        num>>=1
    return c
        
    
num=int(input())
print(SetBits(num))
#remove last setbit
def RemoveLastSetBit(num):
    # ans=''
    num=num&num-1
    return num
num=int(input())
print(RemoveLastSetBit(num))
#toggle the ith bit
def toggle(num,ith):
    mask=1<<ith
    num=num^mask
    return num
num=int(input())
ith=int(input())
print(toggle(num,ith))
#set the ith bit
def Set(num,ith):
    mask=1<<ith
    num=num | mask
    return num
num=int(input())
ith=int(input())
print(Set(num,ith))
# ith bit is set or not
num=int(input())
ith=int(input())
if ((num>>ith)&1)==1:
    print('set')
else:
    print('unset')

#powerset print all the subsets n number have 2**n subsets
def PowerSet(arr):
    size=len(arr)
    subset= 1<<size
    ans=[]
    for num in range(subset):
        curr=[]
        for i in range(size):
            if num & (1<<i):
                curr.append(arr[i])
        ans.append(curr)
    return ans
arr=list(map(int,input().split()))
print(PowerSet(arr))
#simple number print the number which appeared once
def SimpleNum(num):
    n=len(num)
    xor=0
    for i in range(0,n):
        xor=xor^num[i]
    return xor
num=list(map(int,input().split()))
print(SimpleNum(num))
# other approch for it
def simple(nums):
    # n=len(nums)
    hash={}
    for num in nums:
        hash[num]=hash.get(num,0)+1
    for k,v in hash.items():
        if v==1:
            return k
    return -1
nums=list(map(int,input().split()))
print(simple(nums))


'''
# # find the xor of all given numbers from 1 to n
def xorr(n):
    if n%4==1:
        return 1
    elif n%4==2:
        return n+1
    elif n%4==3:
        return 0
    else:
        return n
# n=int(input())
# print(xor(n))
# find xor from l to n
def xor(l,r):
    # xor1=0
    # xor2=0
    return xorr(l-1)^xorr(r)
    # return ans
l=int(input())
r=int(input())
print(xor(l,r))

