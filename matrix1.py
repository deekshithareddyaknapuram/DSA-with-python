def input_matrix(rows,cols):
    matrix=[]
    print(f'enter elements {rows }x{cols} in marix:')
    for i in range(rows):
        row=list(map(int,input(f'enter {i+1}(space-seperated values):').split()))
        matrix.append(row)
    return matrix
def add_matrices(matrix1,matrix2):
    result=[]
    for i in range(len(matrix1)):
        row=[]
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j]+matrix2[i][j])
        result.append(row)
    return result
rows=int(input('enter the number of rows:'))
cols=int(input('enter number of coloums:'))
print('matrix1:')
matrix1=input_matrix(rows,cols)
print('\nMatrix2:')
matrix2=input_matrix(rows,cols)
result=add_matrices(matrix1,matrix2)
print('\nMatrix1:')
for row in matrix1:
    print(row)
print('\nMatrix2:')
for row in matrix2:
    print(row)
print('\nResult of Matrix Addition:')
for row in result:
    print(row)