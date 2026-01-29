def leftover_string(A,B):
    remove_chars=set(B)
    result=(char for char in A if char not in remove char)
    leftover=''.join(result)
    print(result)

    # for char in A:
    #     if char not in remove_chars:
    #         leftover+=char
    # if leftover:
    #     return leftover
    # else:
    #     return 'empty'
    return leftover if leftover else 'empty'
A=input()
B=input()
leftover_string(A,B)

