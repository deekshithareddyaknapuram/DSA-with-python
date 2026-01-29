def MaxProductSubarray(arr):
    maxi=float("-inf")
    pref=1
    suff=1
    n=len(arr)
    for i in range(0,n):
        if pref==0:
            pref=1
        if suff==0:
            suff=1
        pref=pref*arr[i]
        suff=suff*arr[-1]
        maxi=max(maxi,max(pref,suff))
    return maxi
arr=list(map(int,input().split()))
print(MaxProductSubarray(arr))