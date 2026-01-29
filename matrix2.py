def spiral(n):
  #  matrix=[[0]*n for k in range(n)]
    rs,re=0,n-1
    cs,ce=0,n-1
    result=[]
    while rs<=re and cs <=ce:
        for i in range(cs,ce+1):
            result.append(matrix[rs][i])
            rs+=1
            # rs+=1
            for i in range(rs,re+1):
               result.append[i][ce]
               ce-=1
            # ce-=1
            if rs<=re:
                for i in range(ce,cs-1,-1):
                    result.append(matrix[re][i])
                    # c+=1
                    re-=1
            if cs<=ce:
                for i in range(re,rs-1,-1):
                    result.append(matrix[i][cs])
                    # c+=1
                cs+=1
    return result
n=int(input('enter size of matrix'))
matrix=[]
print('enter matrix row wise')
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
spiral_order=spiral(matrix,n)
print('\nspiral order traversal:')
# for row in spiral_ma:
print(spiral_order)       
            