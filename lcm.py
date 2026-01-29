def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(n1,n2):
    if n1<0:
        n1=-n1
    if n2<0:
        n2=-n2
    return(n1*n2)//gcd(n1,n2)
n1=4
n2=6
print(gcd(n1,n2))
print(lcm(n1,n2))