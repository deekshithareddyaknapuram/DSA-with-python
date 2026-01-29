n=int(input())
# m=int(input())
matrix=[]
# list(map(int,input().split()))
for _ in range(n):
    matrix.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
for i in range(n):
    
        matrix[i].reverse()
print(matrix)
 
