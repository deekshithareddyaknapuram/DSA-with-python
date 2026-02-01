#MinBitflip to covert a number
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
