def count_special_subarray(arr,n):
    c=0
    for i in range(n-2):
        if arr[i]+arr[i+2]==arr[i+1]:
            c+=1
    return c
n=9
arr=[1,2,1,-1,-2,4,4,7,3]
print(count_special_subarray(arr,n)) 