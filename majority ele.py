#majority element >n//2
def maj(arr):


    # arr=list(map(int,input().split()))
    hash={}
    n=len(arr)
    for num in arr:
        hash[num]=hash.get(num,0)+1
        if hash[num]>n//3:
            return num
arr=list(map(int,input().split()))
print(maj(arr))
'''def maj(arr):
    ele=None
    c=0
    for num in arr:
        if c==0:
            ele=num
        if num==ele:
            c+=1
        else:
            c-=1
    return ele
arr=list(map(int,input().split()))
print(maj(arr))'''
#majority element n//3
# def 