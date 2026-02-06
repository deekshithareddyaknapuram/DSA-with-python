def palindrome(s,i=0):
    n=len(s)
    if i>=n//2:
        return True
    if s[i]!=s[n-i-1]:
        return False
    return palindrome(s,i+1)
s=input()
print(palindrome(s))

