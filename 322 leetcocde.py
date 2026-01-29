#you are given an integer array coins representing coins of different demoninations and an interger amount represting a total mount of money return the fewst number of coins that you need to make up that amount .if that amount of money annot be made up by any combinatiob of the coins ,return-1
#you may assume that you have an infinite number of each kind of coin
#eg1 
#input coins=[1,2,5],amount=11
#output
# explanation:11=5+5+1
# eg2:
 # input:coins=[2],amount=3 
class Solution:

   def coins(self,coin,amount):
       dp=[amount+1]*(amount+1)
       dp[0]=0
       for i in coin:
           for j in range(i,amount+1):
               dp[j]=min(dp[j],dp[j-1]+1)
       if dp[amount]!=amount+1:
           return dp[amount]
       else:
           return-1