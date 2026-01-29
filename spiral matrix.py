def spiral(n):
    # n=int(input())


    matrix=[[0]*n for _ in range(n)]
    # n=len(matrix)
    top=0
    left=0
    right=n-1
    bottom=n-1
    nums=1
    while left<=right and top<=bottom:
        for i in range(left,right+1):
            matrix[top][i]=nums
            nums+=1
        top+=1
        for i in range(top,bottom):
            matrix[i][right]=nums
            nums+=1
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                matrix[bottom][i]=nums
                nums+=1
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                matrix[i][left]=nums
                nums+=1
            left+=1
    return matrix
n=int(input())
spiral_matrix=spiral(n)
for row in spiral_matrix:
    print(row)
