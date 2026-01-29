
def removeKdigits(num,k):
    st=[]
    for i in num:
        while st and k>0 and st[-1]>i:
            st.pop()
            k-=1
        st.append(i)
    while k>0:
        st.pop()
        k-=1
    res="".join(st).lstrip("0")
    if res:
     return res
    else:
        return "0"
num='1432219'
k=3
print(num,k)    