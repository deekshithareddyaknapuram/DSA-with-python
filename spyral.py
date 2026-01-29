def spiral(n):
    matrix=[[0]*n for kk in range(n)]
    rs,re=0,n-1
    cs,ce=0,n-1
    c=1
    while rs<=re and cs <=ce:
        for i in range(cs,ce+1):
            matrix[rs][i]=c
            c+=1
            rs+=1
            for i in range(rs,re+1):
               matrix[i][ce]=c
               c+=1
            ce-=1
            if rs<=re:
                for i in range(ce,cs-1,-1):
                    matrix[re][i]=c
                    c+=1
                    re-=1
            if cs<=ce:
                for i in range(re,rs-1,-1):
                    matrix[i][cs]=c
                    c+=1
                cs+=1
    return matrix
n=int(input('enter size of spiral'))
spiral_matrix=spiral(n)
for row in spiral_matrix:
    print(row)       
            

