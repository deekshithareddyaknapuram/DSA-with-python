def subseq(i,arr,temp):
    if i==len(arr):
        print(temp)
        return
    subseq(i+1,arr,temp+[arr[i]])
    subseq(i+1,arr,temp)
arr=list(map(int,input().split()))
subseq(0,arr,[])