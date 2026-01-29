'''def subarray(nums,k):
    hash={}
    hash[0]=1
    c=0
    xor=0
    for num in nums:
        xor^=num
        x=xor^k
        if x in hash:
            c+=hash[x]
        hash[xor]=hash.get(xor,0)+1
    return c
# nums=list(map(int,input().split()))
# k=int(input())
'''
def countSubarraysWithXorK(arr, k):
    freq = {}
    freq[0] = 1   # important initialization

    xor_sum = 0
    count = 0

    for num in arr:
        xor_sum ^= num

        target = xor_sum ^ k
        if target in freq:
            count += freq[target]

        freq[xor_sum] = freq.get(xor_sum, 0) + 1

    return count
arr=list(map(int,input().split()))
k=int(input())
print(countSubarraysWithXorK(arr,k))