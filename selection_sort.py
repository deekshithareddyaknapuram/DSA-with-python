def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        lower=i
        for j in range(i+1,n):
            if arr[j]<arr[lower]:
                lower=j
            arr[i],arr[lower]=arr[lower],arr[i]
arr=list(map(int,input().split()))
selection_sort(arr)
print('sorted array',arr)