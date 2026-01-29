import random
numbers=random.randint(1,10)
print('guess any number between 1 to 10')
level=input('choose easy or hard level:')
attempts=0
# for attempts in range(0,10):
if level=='hard':
    for attempts in range(0,5):
        print(f'you have 5 attempts')
        guess_number=int(input('guess the number:'))
        if guess_number<numbers:
            print('your guess is low')
        elif guess_number>numbers:
            print('your guess is high')
        
            # return attempts-1

        else:
            print('coreect guess') 

elif level=='easy':
    for attempts in range(0,10):
        print(f'you have 10 attempts')
        guess_number=int(input('guess the number:'))
        if guess_number<numbers:
            print('your guess is low')
        elif guess_number>numbers:
            print('your guess is high')
        
                # r attempts-1

        else:
            print('correct guess') 
else:
    print('enter correctly')

