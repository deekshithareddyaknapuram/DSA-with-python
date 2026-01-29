def largestrecArea(heights):
    st=[]
    ma=0
    for i,h in enumerate(heights):
        start=i
        while st and st[-1][1]>h:
            idx,height=st.pop()
            ma=max(ma,height*(i-idx))
        st.append((start,h))
    n=len(heights)
    for idx,heights in st:
        ma=max(ma,height*(n-idx))
    return ma
heights=list(map(int,input().split()))
print(largestrecArea(heights))