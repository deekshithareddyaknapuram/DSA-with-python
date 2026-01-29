def astroid(astroids):
    st=[]
    for ast in astroids:
        while st and ast<0 and st[-1]>0:
            if st[-1]<-ast:
                st.pop()
                continue
            elif st[-1]==-ast:
                st.pop()
            break
        else:
            st.append(ast)
    return st
astroids=list(map(int,input().split()))
print(astroid(astroids))

