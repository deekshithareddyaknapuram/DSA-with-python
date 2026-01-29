# given two strings A and B your take is to find and return a string representing thw e left over string in A after removing all the letters that exist in string B. return 'empty' if the output does not contain any value
# A='ABCDEF'
# B='BDE'
# output
# ACF
def leftover_string(A,B):
    remove_chars=set(B)
    leftover=''
    for char in A:
        if char not in remove_chars:
            leftover+=char
    if leftover:
        return leftover
    else:
        return 'empty'
A=input()
B=input()
print('leftover_string',A,B)
