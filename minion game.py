def minion_game(string):
    vowels="AEIOU"
    KEVINS_SCORE=0
    STUART_SCORE=0
    for i in range(len(string)):
        if string[i] in vowels:
            KEVINS_SCORE+=len(string)-i
        else:
            STUART_SCORE+=len(string)-i
    if KEVINS_SCORE>STUART_SCORE:
        print('Kevin',KEVINS_SCORE)
    elif STUART_SCORE>KEVINS_SCORE:
        print('Stuart',STUART_SCORE)
    else:
        print('Draw')
# minion_game(string)

