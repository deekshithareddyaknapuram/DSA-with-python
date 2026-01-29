import random as rand 










print('The number between 1 or 50')

type=input('choose easy or hard level:')
if type=='hard':
    guess=int(input('guess the number:'))
    for i in range(0,guess-1):
     print('you have 5 attempts')


elif type=='easy':
    print('you have 10 attempt')
else:
    print('enter correctly')
