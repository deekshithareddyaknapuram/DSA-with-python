'''def lcs(s1,s2,m,n):
   if m==0 or n==0 or s1[m-1]!=s2[n-1]:
     return 0
   return 1+lcs(s1,s2,m-1,m-2)
def maxcommonstr(s1,s2):
   res=0
   m=len(s1)
   n=len(s2)
   for i in range(1,m+1):
      for j in range(1,n+1):
         res=max(res,lcs(s1,s2,i,j))
   return res
s1='abcdxyz'
s2='xyzabcd'
print(maxcommonstr(s1,s2))'''
#bottom up
'''def maxCommonStr(s1,s2):
   m=len(s1)
   n=len(s2)
   lcs=[[0]*(n+1)for _ in range(m=1)]
   res=0
   for i in range(1,m+1):
      for j in range(1,n+1):
        if s1[i-1]==s2[j-1]:
            lcs[i][j]=lcs[i-1][j-1]+1
            res=max(res,lcs[i][j])
        else:
           lcs[i][j]=0
   return res
s1='abcdxyz'
s2='xyzabcd'
print(maxCommonStr(s1,s2))'''
#space optimization
def lcs(s1,s2):
   m=len(s1)
   n=len(s2)
   #create 1D array to stor prev rows result
   prev=[0]*(n+1)
   res=0
   for i in range(1,m+1):
      # create tem arr to store current row
      curr=[0]*(n+1)
      for j in range(1,n+1):
         if s1[i-1]==s2[j-1]:
            curr[j]=prev[j-1]+1
            res=max(res,curr[j])
         else:
            curr[j]=0
        #move curr row data to prev row 
   prev=curr
   return res
s1='abcdxyz'
s2='xyzabcd' 
print(lcs(s1,s2))

