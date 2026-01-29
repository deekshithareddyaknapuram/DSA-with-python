def mergeTwoSortedArrays(arr1,arr2):
    arr1.sort()
    arr2.sort()
    
    n=len(arr1)
    m=len(arr2)
    a=n-1
    b=0
    while a>=0 and b<m:
        if arr1[a]>arr2[b]:
            arr1[a],arr2[b]=arr2[b],arr1[a]
            a-=1
            b+=1
        else:
            break
    arr1.sort()
    arr2.sort()
    return arr1,arr2
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
# n=len(arr1)
# m=len(arr2)
a,b=mergeTwoSortedArrays(arr1,arr2)
print(a)
print(b)