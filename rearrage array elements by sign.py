nums=list(map(int,input().split()))
ans=[0]*len(nums)
pos_indx=0
neg_indx=1
for i in range(0,len(nums)):
    if nums[i]>0:
        ans[pos_indx]=nums[i]
        pos_indx+=2
    else:
        ans[neg_indx]=nums[i]
        neg_indx+=2
print(ans)