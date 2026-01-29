def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input('enter 1st num'))
b=int(input('enter 2nd num'))
print(gcd(a,b))