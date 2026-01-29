def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr=list(map(int,input().split()))
insertion_sort(arr)
print('sorted array',arr)
#divide and conquere:divide the problem into subpbroblems and solving them indiviually and using those individual solutions we need to obtain the main problem solution.