def max_score_subarray(n,k,a):
    max_score=0
    for i in range(n-k+1):
        current_score=0
        for j in range(k):
            current_score+=(j+1)*a[i+j]
        max_score=max(max_score,current_score)
    return max_score
n=int(input()) 
k=int(input())
a=list(map(int,input().split()))
print(max_score_subarray(n,k,a))
