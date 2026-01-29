# import numpy as np 
def input_matrix(rows,cols):
    matrix=[]
    print(f'{rows}x{cols}matrix:')
    for i in range(rows):
        row=list(map(int,input(f'enter row{i+1}(space_seperated values:)').split()))
        matrix.append(row)
        return np. array(matrix) # type: ignore
    rows=int(input('enter rows:'))
    cols=int(input('enter cols:'))
    print('matrix1:')
    matrix1=input_matrix(row,cols)
    print('\nMatrix2:')
    Matrix2=input_matrix(rows,cols)
    result=matrix1+Matrix2
    print('\nMatrix1:',matrix1)
    print('\nmatrix2',Matrix2)
    print(result)
