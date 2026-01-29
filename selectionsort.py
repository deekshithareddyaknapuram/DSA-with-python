def section(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
            arr[i],arr[min]=arr[min],arr[i]
arr=list(map(int,input().split()))
print(section(arr))
