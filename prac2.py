# n=int(input())
# order=len(str(n))
# sum=0
# temp=n
# while temp>0:
#     digit=temp%10 #3
#     sum+=digit**order
#     temp=temp//10
# if sum==n:
    
#     print('armstrong')
#     # break
# else:
    
#     print('no')
#     # break
n=int(input())
for i in range(0,51):
    if i%3==0 and i%5==0:
        print(n,'FizzBuss')
    elif i%3==0:
        print(n,'Fizz')
    elif i%5==0:
        print(n,'Buss')
    else:
        print(n,'NOT VALID')
