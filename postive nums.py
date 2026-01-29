nums=list(map(int,input().split()))
res=[]
while nums>0:
    for num in nums:
        if nums%2==0:
            res.append(nums)
        print(res)
