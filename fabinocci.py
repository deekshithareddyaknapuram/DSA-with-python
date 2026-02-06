def fabinocci(num):
    n=num
    if n<=1:
        return n
    last=fabinocci(n-1)
    s_last=fabinocci(n-2)
    return last+s_last
num=int(input())
for i in range(num):

    print(fabinocci(i),end=' ')