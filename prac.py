# # check num +,-,0
# def check(n):
#     if n>0:
#         print('positive')
#     elif n<0:
#         print('negative')
#     else:
#         print('zero')
# # check(n)
# n=int(input('enter num'))
# print(check(n))
# # print(r)
# n=int(input())
# for n in range(1,21):
#     # if n<20:
#     #     None
#     if n%2!=0:
#         print('odd')
#         break
#     # else:
#     #     print('even')
#     #     break
#     #     # return None
# 
# def rev():
#  s=input('')
#  rev_s=s[::-1]
#  print(rev_s())
# rev()
# count number of vowels in string
# def c_vowels():
#     c=0
#     for vowels in string.lower():
#         if vowels in 'aeiou':
#             c+=1
#     return c
# string=input()
# print(c_vowels())
# check palindrome
# def is_palindrome(string):
#     return string==string[::-1]
# string=input()
# print(is_palindrome(string))
# def numbers():
#     s=0
#     for i in nums:
#         s=numbers(i)


# nums=int(input())
# print(numbers()) 
           
# n=list(map(int,input().split(',')))
# print(sum(n))
# def char(name,letter):
#     c=0
#     for i in name:
#         if i==letter:
#             c+=1
#         # c+=1
#     return c
# name=input()
# letter=input()
# print(char(name,letter))
# def c_vowels():
#     c=0
#     for vowels in string:
#         if vowels in 'aeiou':
#             c+=1
#     return c
        
#         # c+=1
# string=input()
# print(c_vowels())
# find the largest num
# def find_max():
#     max_num=arr[0]
#     for i in range(0,n):
#         if arr[i]>max_num:
#             max_num=arr[i]
#     return max_num
# arr=list(map(int,input().split(' ')))
# n=len(arr)
# print(find_max())
# def is_prime(n):
#     if n<=1:
#         return False
    
        
#     for i in range(2,n):
#         if n%i==0:
#             return False
            
#     return True 
# n=int(input())
# if is_prime(n):
#     print(n,'its prime')
# else:
#     print(n,'its not prime')
# reverse of string
# def rev_string(s):
#     rev=''
#     for char in  s:
#         rev=char+rev
#     return rev
# s=input()
# print(rev_string(s))
# dictionary
# def c_letters(s):
#     dict={}
#     for char in s:
#         if char in dict:
#             dict[char]+=1
#         else:
#             dict[char]=1
#     return dict
# s=input()
# print(c_letters(s))
# n=list(map(int,input().split(',')))
# re=sum(n)
# print(re)
# def sum_of_numbers():
#     total=0
#     for num in numbers:
#         total+=num
#     return total
# numbers=list(map(int,input().split(',')))
# print(sum_of_numbers())
# def is_palindrome(s):
#     st=''
#     st==s[::-1]
#     return st
# s=input()
# if is_palindrome(s):
 
#  print('palindome',is_palindrome(s))
# else:
#    print('not a palindrome',is_palindrome(s))
# print all numbers from 1 to n skip multiples of 3
# num=list(map(int,input().split(' ')))
# for i in num:
#     if i%3==0:
#         continue
#     else:
#         print(i)
# string=input()
# print(string.upper())

# def check(s):
#     for char in s:
#         if char in 'aeiou':
#             return 'vowel'
#         return 'consonent'
        
# s=input()
# print(check(s))
# def reverse(s):
#     rev=''
#     for char in s:
#         rev=char+rev
#     return rev
# s=input()
# print(reverse(s))
# sum of digits
# n=int(input())
# total=0
# while n>0:
#     d=n%10
#     total=total+d
#     n=n//10
# #  n=list(map(int,input()))
# # sum(n)
# print(total)

# by using recursion
# palindrome
# def is_palindrome(s):
#     return s==s[::-1]
# s=input()
# print(is_palindrome(s)) 
# find max
# def maxi(arr):
#     max_num=0
#     for i in range(1,n):
#         if arr[i]>max_num:
#             max_num=arr[i]
#     return max_num
# arr=list(map(int,input().split(',')))
# n=len(arr)
# print(maxi(arr))
# # by using built in func
# arr=list(map(int,input().split(',')))
# print(max(arr))
# fact of a num
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     return f
# n=int(input())
# print(fact(n))
# armstrong method
n=int(input())
order=len(str(n))
sum=0
temp=n
while n>0:
    digit=temp%10 #3
    sum+=digit**order
    temp=temp//10
if sum==n:
    print('armstrong')
else:
    print('no')

