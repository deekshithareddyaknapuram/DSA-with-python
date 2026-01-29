def tower(n,source,aux,des):
    if n==1:
        print(f'move disc 1 from{source} to {des}')
        return
    tower(n-1,source,des,aux)
    print(f'move disk{n} from{source} to{des}')
    tower(n-1,aux,source,des)
n=int(input())
tower(n,'a','b','c')
