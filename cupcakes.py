n=int(input())
a=list(map(int,input().split()))

def sum(n,a):
    t_cupcakes=0
    for cupcakes in a :
     if cupcakes>=5:
        t_cupcakes+=cupcakes
    print(t_cupcakes)
    return t_cupcakes



sum(n,a)